#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: test_math.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-06-09
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""

from math import add


def assert_equal(a, b):
    if a == b:
        return True
    raise Exception("Failed")


def test_add():
    assert_equal(add(2, 2), 4)
    assert_equal(add(2, 3), 5)


def test():
    """docstring for test"""
    test_add()

if __name__ == "__main__":
    test()
