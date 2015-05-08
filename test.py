#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

'''
    File name: test.py
    Version: 0.1
    Author: dhilipsiva <dhilipsiva@gmail.com>
    Date created: 2015-04-11
'''
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""


def ISBNcode(data):
    code = [int(x) for x in data]
    result = 0
    for i in range(1, 13):
        if i % 2 == 0:
            multiple = 3
        else:
            multiple = 1
        result += code[i-1] * multiple
    code.append(10 - result % 10)
    print code
    print "".join([str(x) for x in code])


user = str(input("Enter the 12 digit ISBN code : "))
ISBNcode(user)
