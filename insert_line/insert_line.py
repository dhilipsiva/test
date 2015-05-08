#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: insert_line.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-04-21
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""


def insert_text(file_path, search_text, before_text, after_text):
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    f = open(file_path, "w")
    for line in lines:
        if search_text in line:
            f.write(before_text)
        f.write(line)
        if search_text in line:
            f.write(after_text)
    f.close()


# Example:
insert_text("sample.c", "target_function", "// Before function\n", "// After function\n")
