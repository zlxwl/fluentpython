# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 下午3:31
# @Author  : Zhong Lei
# @FileName: flags_commons.py
import os
import time
import sys
import string
import argparse
from collections import namedtuple
from enum import Enum

Result = namedtuple('Result', 'status data')

HTTPStatus = Enum('Status', 'ok not_found error')

POP20_CC = ('CN', 'IN', 'US', 'ID', 'BR', 'PK', 'NG', 'BD', 'RU', 'JP', 'MX', 'PH', 'VN', 'ET', 'DE', 'IR', 'CD', 'FR')

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 20

SERVERS = {
    'REMOTE': 'http://flupy.org/data/flags',
    'LOCAL': 'http://localhost:8001/flags',
    'DELAY': 'http://localhost:8002/flags',
    'ERROR': 'http://localhost:8003/flags'
}

DEFAULT_SERVER = 'REMOTE'

DEST_DIR = 'downloads/'

COUNTRY_CODES_FILE = 'country_codes.txt'


def save_flags(img, file_name):
    path = os.path.join(DEST_DIR, file_name)
    if not os.path.exists(DEST_DIR):
        os.mkdir(DEST_DIR)
    with open(path, 'wb') as f:
        f.write(img*10)


def initial_report(cc_list, actual_req, server_label):
    if len(cc_list) <= 10:
        cc_msg = ', '.join(cc_list)
    else:
        cc_msg = 'from {} to {}'.format(cc_list[0], cc_list[1])

    print('{} site: {}'.format(server_label, SERVERS[server_label]))

    msg = 'Searching for {} flag{}: {}'
    plural = 's' if len(cc_list) != 1 else ''
    print(msg.format(len(cc_list), plural, cc_msg))

    plural = 's' if actual_req != 1 else ''
    msg = '{} concurrent connection{} will be used.'
    print(msg.format(actual_req, plural))


def final_report(cc_list, counter, start_time):
    elapsed = time.time() - start_time
    print('-' * 20)
    msg = '{} flag{} downloaded'
    plural = 's' if counter[HTTPStatus.ok] != 1 else ''
    print(msg.format(counter[HTTPStatus.ok], plural))

    if counter[HTTPStatus.not_found]:
        print(counter[HTTPStatus.not_found], plural)

    if counter[HTTPStatus.error]:
        plural = 's' if counter[HTTPStatus.error] != 1 else ''
        print('{} error{}.'.format(counter[HTTPStatus.error], plural))

    print('Elapsed time {:.2f}s'.format(elapsed))


def expand_cc_args(every_cc, all_cc, cc_args, limit):
    codes = set()
    A_Z = string.ascii_uppercase
    if every_cc:
        codes.update(a+b for a in A_Z for b in A_Z)
    elif all_cc:
        with open(COUNTRY_CODES_FILE) as fp:
            text = fp.read()
        codes.update(text.split())
    else:
        for cc in (c.upper() for c in cc_args):
            if len(cc) == 1 and cc in A_Z:
                codes.update(cc + c for c in A_Z)
            elif len(cc) == 2 and all(c in A_Z for c in cc):
                codes.add(cc)
            else:
                msg = 'each cc argument must be A to Z or AA to ZZ'
                raise ValueError('*** Usage error:', + msg)
    return sorted(codes)[:limit]


def process_args(default_concur_req):
    server_options = ''.join(sorted(SERVERS))
    parser = argparse.ArgumentParser(
        description='Download flags for country codes.'
                    'Default: top 20 countries by pop')
    parser.add_argument('cc', metavar='CC', nargs='*', help='country code or 1st letter(eg. B for BA...BZ)')
    parser.add_argument('-a', '--all', action='store_true', help='get all available flags (AD to ZW)')
    parser.add_argument('-e', '--every', action='store_true', help='get flag for every possible code(AA...ZZ)')
    parser.add_argument('-l', '--limit', metavar='N', type=int, help='limit to N first codes', default=sys.maxsize)
    parser.add_argument('-m', '--max_req', metavar='CONCURRENT', type=int, default=default_concur_req,
                        help='maximum concurrent request (default{})'.format(default_concur_req))
    parser.add_argument('-s', '--server', metavar='LABEL', default=DEFAULT_SERVER,
                        help='Server to hit; one of {} (default{})'.format(server_options, DEFAULT_SERVER))
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.max_req < 1:
        print('*** Usage error: --max_req CONCURRENT must be >=1')
        parser.print_usage()
        sys.exit(1)
    if args.limit < 1:
        print('*** Usage error: --limit N must be >=1')
        sys.exit(1)
    args.server = args.server.upper()
    if args.server not in SERVERS:
        print('*** Usage error: --server LABEL must be one of ')
        parser.print_usage()
        sys.exit(1)
    try:
        cc_list = expand_cc_args(args.every, args.all, args.cc, args.limit)
    except ValueError as exc:
        print(exc.args[0])
        parser.print_usage()
        sys.exit(1)
    if not cc_list:
        cc_list = sorted(POP20_CC)
    return args, cc_list


def main(download_many, default_concur_req, max_concur_req):
    args, cc_list = process_args(default_concur_req)
    actual_req = min(args.max_req, max_concur_req, len(cc_list))
    initial_report(cc_list, actual_req, args.server)
    base_url = SERVERS[args.server]
    t0 = time.time()
    counter = download_many(cc_list, base_url, args.verbose, actual_req)
    assert sum(counter.values()) == len(cc_list), 'some downloads are unaccounted for'
    final_report(cc_list, counter, t0)
