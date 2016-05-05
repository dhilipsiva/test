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
Date created: 2016-05-02
"""


T = int(raw_input())
lines = []

while T > 0:
    lines.append([int(t) for t in raw_input().split(" ")])
    T -= 1

for line in lines:
    N = _min = min(*line)

    line = [x-N for x in line]
    for num in line:
        N += int(num / 3)

    line = [x % 3 for x in line]
    if sum(line) > 3 and _min > 0:
        N += 1

    print N
