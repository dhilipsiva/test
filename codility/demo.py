#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: demo.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-06-29
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""
https://codility.com/c/run/demoCJKQPY-9N2
"""


def solution(A):
    for i in xrange(len(A)):
        if sum(A[:i]) == sum(A[i+1:]):
            return i
    return 0

A = [-1, 3, -4, 5, 1, -6, 2, 1]
print solution(A)
