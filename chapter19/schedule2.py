# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 上午11:46
# @Author  : Zhong Lei
# @FileName: schedule2.py
import warnings
import inspect
from chapter19 import osconfeed

DB_NAME = '/home/zhonglei/PycharmProjects/fluentpython/chapter19/data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            raise NotImplemented


class MissingDataBaseError(RuntimeError):
    '''
    需要数据库，但没有指定数据库时抛出
    '''


class DbRecord(Record):
    __Db = None

    @staticmethod
    def set_db(db):
        DbRecord.__Db = db

    @staticmethod
    def get_db():
        return DbRecord.__Db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDataBaseError(msg.format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()


class Event(DbRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key)) for key in spkr_serials]
            return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)


if __name__ == '__main__':
    import shelve
    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        load_db(db)
    DbRecord.set_db(db)

    event = DbRecord.fetch('event.33950')
    print(event)
    print(event.venue)
    print(event.venue.name)
    for skr in event.speakers:
        print('{0.serial}: {0.name}'.format(skr))
