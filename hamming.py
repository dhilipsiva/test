#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: hamming.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-04-24

2**i * 3**j * 5**k
i>=j>=k>=0
"""

hamming_dict = {}
numbers = []

nth = int(input())


def hamming(i, j, k):
    return (2**i) * (3**j) * (5**k)


for k in range(0, 10):
    for j in range(0, 10):
        for i in range(0, 10):
            args = [i, j, k]
            hamming_number = hamming(*args)
            numbers.append(hamming_number)
            hamming_dict[hamming_number] = args

numbers = sorted(numbers)
print(numbers[nth-1])
