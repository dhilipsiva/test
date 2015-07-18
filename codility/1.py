#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: 1.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-06-30
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""


def solution(X, A):
    for i in range(1, len(A)):
        second = A[i:]
        if A[:i].count(X) == (len(second) - second.count(X)):
            return i
    return 0

A = [5, 5, 1, 7, 2, 3, 5]
print solution(5, A)
