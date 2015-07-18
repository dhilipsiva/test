#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: enums2.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-07-07
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""
import inspect


def user_attributes(cls):
    defaults = dir(type('defaults', (object,), {}))  # gives all inbuilt attrs
    return [
        item[0] for item in inspect.getmembers(cls) if item[0] not in defaults]


def choices(cls):
    """
    Decorator to set `CHOICES` and other attributes
    """
    _choices = []
    for attr in user_attributes(cls):
        val = getattr(cls, attr)
        setattr(cls, attr[1:], val[0])
        _choices.append((val[0], val[1]))
    setattr(cls, 'CHOICES', tuple(_choices))
    return cls


class BazEnum():
    _BAZ = [2, "Some Baz String"]


@choices
class FooEnum(BazEnum):
    _FOO = [1, "Some Foo String"]
    _BAR = [2, "Some Bar String"]

print FooEnum.CHOICES
print FooEnum.FOO
print dir(FooEnum)
