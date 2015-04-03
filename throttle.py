#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Copyright © Appknox
#

'''
    File name: throttle.py
    Version: 0.1
    Author: dhilipsiva <dhilipsiva@gmail.com>
    Date created: 2015-03-11
'''
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""

import time

start = time.time()
while True:
    delta = time.time() - start
    if delta > 1:
        print "----- Foo -----"
        start = time.time()
