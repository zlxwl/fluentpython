# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 上午11:13
# @Author  : Zhong Lei
# @FileName: flags_threadpool.py
from concurrent import futures
from chapter17.flags import save_flag, get_flag, show, main, POP20_CC

MAX_WORKERS = 20


def download_one(cc):
    img = get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc


# threadpool
# def download_many(cc_list):
#     workers = min(MAX_WORKERS, len(cc_list))
#     with futures.ThreadPoolExecutor(workers) as executor:
#         res = executor.map(download_one, cc_list)
#     return len(list(res))


# processpool
def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, cc_list)
    return len(list(res))


if __name__ == '__main__':
    main(download_many)