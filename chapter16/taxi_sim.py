# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 上午11:45
# @Author  : Zhong Lei
# @FileName: taxi_sim.py
from collections import namedtuple
import queue
import random
import collections
import argparse
import time
from typing import Dict

Event = namedtuple('Event', 'time proc actions')

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5


def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passengers')
        time = yield Event(time, ident, 'drop off passengers')
    yield Event(time, ident, 'going home')


class Simulator:
    def __init__(self, procs_map: Dict):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, procs in sorted(self.procs.items()):
            first_event = next(procs)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '  ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def compute_duration(previous_actions):
    if previous_actions in ['leave garage', 'drop off passengers']:
        interval = SEARCH_DURATION
    elif previous_actions == 'pick up passengers':
        interval = TRIP_DURATION
    elif previous_actions == 'going home':
        interval = 1
    else:
        raise ValueError('Unknow previous_action: %s' % previous_actions)
    return int(random.expovariate(1/interval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    if seed is not None:
        random.seed(seed)
    taxi = {
        i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL) for i in range(num_taxis)
    }
    sim = Simulator(taxi)
    sim.run(end_time)


if __name__ == '__main__':
    # taxi = taxi_process(ident=13, trips=2, start_time=0)
    # print(next(taxi))
    # taxi.send(7)
    # print(taxi)
    main(DEFAULT_END_TIME)