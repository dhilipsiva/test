#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Copyright © dhilipsiva
#

'''
    File name: sqlite2xls.py
    Version: 0.1
    Author: dhilipsiva <dhilipsiva@gmail.com>
    Date created: 2015-04-03
'''
__author__ = "dhilipsiva"
__status__ = "development"

"""
Convert an SQlite database to an XLS (excel) spreadsheet.

pip install xlwt

Originally taken from: https://github.com/flow-phys/sqlite2xls
"""

import sqlite3 as lite
import xlwt
import sys
import math

db = sys.argv[1]
out = sys.argv[2]

con = lite.connect(db)
cur = con.cursor()


# Get all the tables in this database
cmd = "select name from sqlite_master where type = 'table' "
cur.execute(cmd)
tables = cur.fetchall()


workbook = xlwt.Workbook()
for table in tables:
    # Get column heads
    cur.execute('pragma table_info(%s)' % table[0])
    head = cur.fetchall()
    # Get row entries
    cur.execute('select * from %s' % table[0])
    players = cur.fetchall()

    Np = len(players)
    cmax = 30000     # Max character per cell
    Rmax = 64000     # Max number of rows per sheet
    NS = 1
    if (Np > Rmax):
        NS = int(math.ceil(float(Np)/float(Rmax)))
    for ss in range(NS):
        ips = ss*(Rmax)
        ipe = min((ss+1)*Rmax, Np)
        # Open workbook and save head/body
        print table[0]
        sheet = workbook.add_sheet(table[0][:30])
        for col, item in enumerate(head):
            sheet.write(0, col, item[1])
        # body
        for row, player in enumerate(players[ips:ipe]):
            for col, item in enumerate(player):
                if (type(item) == type(u'')):
                    imax = min(cmax, len(item))
                    sheet.write(row+1, col, item[0:imax])
                else:
                    sheet.write(row+1, col, item)
    # done

workbook.save(out)
