#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: foop.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-05-15
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""


class Foo(object):

    def baz(self):
        """
        docstring for baz
        """
        print "Foo"


class Bar(object):

    def baz(self):
        """
        docstring for baz
        """
        print "Bar"


class Blah(object):

    def baz(self):
        """
        docstring for baz
        """
        print "Blah"


class Baz(Blah, Foo, Bar):
    pass


baz = Baz()

baz.baz()
