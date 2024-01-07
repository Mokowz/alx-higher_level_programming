#!/usr/bin/python3


def std_tup(tup):
    tup_len = len(tup)
    if tup_len == 0:
        return (0, 0)
    elif tup_len == 1:
        return (tup[0], 0)
    else:
        return (tup[0], tup[1])


def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    tup_a_std = std_tup(tuple_a)
    tup_b_std = std_tup(tuple_b)
    sum1 = tup_a_std[0] + tup_b_std[0]
    sum2 = tup_a_std[1] + tup_b_std[1]
    return (sum1, sum2)
