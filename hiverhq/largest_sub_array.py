#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: largest_sub_array.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-10-12
"""

arr = [1, 4, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5]
# arr = raw_input()
# arr = arr.split(", ")
# arr = [int(i) for i in arr]


def print_array(arr):
    print(', '.join(str(i) for i in arr))


def is_all_positive(arr):
    for num in arr:
        if num < 0:
            return False
    return True


def is_all_negative(arr):
    for num in arr:
        if num > 0:
            return False
    return True


def trim_array(arr):
    """
    Recursive function to trim array of negative numbers in the end
    """
    for idx in [0, -1]:
        if arr[idx] < 0:
            arr.pop(idx)
            trim_array(arr)


def remove_negative_sum(arr):
    """
    recursive funtion to find and remove starting sequence that yeilds negative
    value
    """
    _sum = 0
    for idx, num in enumerate(arr):
        _sum += num
        if _sum < 0:
            return remove_negative_sum(arr[idx + 1:])
    return arr


def main():
    if is_all_positive(arr):
        # Print everything if all elements are +ve
        return print_array(arr)

    if is_all_negative(arr):
        # print largest number is everything is negative
        return print_array([max(arr)])

    # Trim -ve numbers in the ends. Does not make any sense to have those.
    trim_array(arr)
    sub_arr = remove_negative_sum(arr)
    sub_arr.reverse()
    sub_arr = remove_negative_sum(sub_arr)
    sub_arr.reverse()
    print_array(sub_arr)

main()
