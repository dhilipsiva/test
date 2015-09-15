#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: favorites.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-07-26
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""

fmt = """		"%i"
		{
			"name"		"%i"
			"gamedir"		"cstrike"
			"Players"		"3"
			"maxplayers"		"32"
			"map"		"de_dust2"
			"address"		"%s"
			"lastplayed"		"0"
			"secure"		"1"
			"type"		"4"
		}\n"""

f = open("ips.txt", "r")
w = open("w.txt", "w")
i = 5
for line in f:
    w.write(fmt % (i, i, line.replace("\n", "")))
    i += 1
