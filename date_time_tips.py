def seconds_difference(time_1, time2):
    '''(float, float) -> float
    Return the number of seconds later
    that a time in seconds time_2 is than
    a time in seconds time_1.
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    '''

def hours_difference(time_1, time_2):
    '''(float, float) -> float
    return the number of hours later that
    a time in seconds time_2 is than a time
    in seconds time_1.
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    '''

import datetime

before = datetime.datetime.now()
after  = datetime.datetime.now()

hours = (after - before).total_seconds() // 3600