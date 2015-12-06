#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: pavi.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-12-06

Requirements:
`pip install xlsxwriter`
"""

import xlsxwriter

file_list = ["tmp.txt", "tmp2.txt"]  # this is list of all the files that needs to be scanned.
xlsx_file = "output.xlsx"  # This is the output excel path. You can also provide full path names here.


def extract_data(input_file):
    contents = open(input_file, "r").read()
    script_name = contents.split("SCRIPT: ")[1].split("\n")[0].split("/")[-1]
    if 'TEST PASSED' in contents:
        result = "PASSED"
    else:
        result = "FAILED"
    return script_name, result


def processs_files(file_list, xlsx_file):
    workbook = xlsxwriter.Workbook()
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for input_file in file_list:
        script_name, result = extract_data(input_file)
        worksheet.write(row, col, script_name)
        worksheet.write(row, col + 1, result)
        row += 1

    workbook.close()


processs_files(file_list, xlsx_file)
