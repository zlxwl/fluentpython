# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 上午10:27
# @Author  : Zhong Lei
# @FileName: schedule.py
import warnings
from chapter19 import osconfeed


DB_NAME = '/home/zhonglei/PycharmProjects/fluentpython/chapter19/data/schedule_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading...')
    for collections, rec_list in raw_data['Schedule'].items():
        record_type = collections[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)


if __name__ == '__main__':
    import shelve
    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        load_db(db)
    print(type(db['speaker.3476']))
    speaker = db['speaker.3476']
    name, twitter = speaker.name, speaker.twitter
    print(name, twitter)


