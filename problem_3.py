import ast
from datetime import datetime
import sys


# s = {"start_time": "2016-01-01 00:00:00", "end_time": "2016-05-01 00:00:00", "overlap": 0}
# s2 = {'start_time': '2016-02-01 00:00:00', 'end_time': '2016-06-01 00:00:00', 'overlap': 0}
# s3 = {"start_time": "2012-01-01 00:00:00", "end_time": "2012-05-01 00:00:00", "overlap": 0}

def main():
    # read stdin
    inputs = [ast.literal_eval(x.strip()) for x in sys.stdin.readlines()]
    n_events = inputs[0]
    events = inputs[1:]

    # if only one event is given, there will be no overlap
    if n_events == 1:
        print(events)
        return

    # remember original order of events, then sort
    oo_events = []
    for idx, line in enumerate(events):
        line['order'] = idx
        oo_events.append(line)
    c = len(oo_events)
    s_events = sorted(oo_events, key=lambda x: datetime.strptime(x['start_time'], '%Y-%m-%d %H:%M:%S'))

    # now that events are sorted by 'start time', we can search for overlaps by comparing
    # the end_date of one event with the start date of the next.
    for i, j in enumerate(s_events):
        if i < c - 1 and datetime.strptime(s_events[i]['end_time'], '%Y-%m-%d %H:%M:%S') > datetime.strptime(
                s_events[i + 1]['start_time'], '%Y-%m-%d %H:%M:%S'):
            oo_events[s_events[i]['order']]['overlap'] = 1
            oo_events[s_events[i + 1]['order']]['overlap'] = 1
        oo_events[s_events[i]['order']].pop('order')

    # output events in original order
    for i in oo_events:
        print(i)


if __name__ == '__main__':
    main()
