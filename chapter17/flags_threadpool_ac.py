# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 上午11:36
# @Author  : Zhong Lei
# @FileName: flags_threadpool_ac.py
from chapter17.flags import get_flag, save_flag, POP20_CC, main, show
from chapter17.flags_threadpool import download_one
from concurrent import futures


def down_load(cc_list):
    cc_list = cc_list[:5]

    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        to_do = []
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(down_load)