#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: curs.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-07-10
"""

import curses
from curses import wrapper, A_REVERSE, start_color


def main(stdscr):
    start_color()
    stdscr.clear()
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
