#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: print_file.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-12-04
"""


def __getattribute__(name):
    print("ATTR: ", name)
    locals()[name]

FOO = "foo"

print(__file__)
