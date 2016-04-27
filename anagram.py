#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: anagram.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-04-24
"""

lines_count = int(raw_input())
lines = []

while lines_count > 0:
    lines.append(raw_input())
    lines_count -= 1


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    set1 = set(word1)
    set2 = set(word2)
    if set1 != set2:
        return False
    count_list1 = [word1.count(a) for a in set1]
    count_list2 = [word2.count(a) for a in set1]
    if count_list1 != count_list2:
        return False
    return True

for line in lines:
    word1, word2 = line.split()
    if is_anagram(word1, word2):
        print("YES")
    else:
        print("NO")
