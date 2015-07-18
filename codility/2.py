#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: 2.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-06-30
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""


def bin_array(limit=1000000):
    i = -1
    while i < limit:
        i += 1
        yield [int(x) for x in bin(i)[2:]]


def calc_number(A):
    if not A:
        return 0
    _sum = 0
    for idx, val in enumerate(A):
        _sum += val * pow(-2, idx)
    return _sum


def solution(A):
    if not A:
        return A
    minus_sum = -calc_number(A)
    for possibility in bin_array():
        if calc_number(possibility) == minus_sum:
            return possibility


print solution([1, 0, 0, 1, 1, 1])
