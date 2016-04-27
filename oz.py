#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: oz.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-04-24
"""

lines_count = int(raw_input())
lines = []

while lines_count > 0:
    lines.append(raw_input())
    lines_count -= 1

inputs = []

for line in lines:
    inputs.append([int(a) for a in line.split(" ")])


def first_4(l):
    min_val = min(l)
    l = [i-min_val for i in l]
    for i in l:
        if i < 3:
            continue
        min_val += int(min_val / 3)
    l = [i % 3 for i in l]
    if min(l) > 0 and sum(l) == 4:
        min_val += 1
    return min_val


def first_others(l):
    min_val = 0
    for i in l:
        if i < 3:
            continue
        min_val += int(i / 3)
    l = [i % 3 for i in l]
    min_val += min(l)
    if sum(l) == 4:
        min_val += 1
    return min_val


for data in inputs:
    fo = first_others(data)
    """
    f4 = first_4(data)
    if fo > f4:
        print(fo)
    else:
        print(f4)
    # print(first_others(data))
    """
    print(fo)
