# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 下午3:49
# @Author  : Zhong Lei
# @FileName: coroaverager3.py
from collections import namedtuple
from typing import Dict

Results = namedtuple('Results', 'count average')


def average():
    count = 0
    average = 0
    total = 0
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Results(count=count, average=average)


def grouper(results: Dict, key: str) -> None:
    while True:
        results[key] = yield from average()


def report(results: Dict):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print(
            '{:2}{:5} averaging {:.2f}{}'.format(
                result.count, group, result.average, unit)
        )


def main(data: Dict) -> None:
    results = {}
    for key, values in data.items():
        group = grouper(results, key=key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)


if __name__ == '__main__':
    data = {
        'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg': [39, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }
    main(data)
