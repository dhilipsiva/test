#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: 3.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-06-30
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""


def solution(A):
    top = True
    right = True
    vertical = True
    point = [0, 0]
    x = 0
    y = 1
    for steps in A:
        if vertical:
            if top:
                point[y] += steps
            else:
                point[y] -= steps
            top = not top
        else:
            if right:
                point[x] += steps
            else:
                point[x] -= steps
            right = not right
        vertical = not vertical
        print point
    """
    Dion, the program is not complete yet. So far, it will only print the
    points. Please let me know If i need to complete this program.
    """
    return 0

A = [1, 3, 2, 5, 4, 4, 6, 3, 2]
print solution(A)
