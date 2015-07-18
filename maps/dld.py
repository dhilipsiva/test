#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: dld.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-07-16
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""
Script to download maps from http://maps.cs-bg.info/
"""

import requests
from pyquery import PyQuery as pq
import StringIO

start_url = "http://maps.cs-bg.info/maps/cs/"
start_url = "http://maps.cs-bg.info/maps/cs/aim/page/8"


def get_page(url):
    """
    docstring for get_page
    """
    print "Getting Map List: ", url
    resp = requests.get(url)
    d = pq(resp.content)
    url = None
    for el in d(".t_maps tr"):
        try:
            d1 = pq(el)
            url = d1("a:eq(1)").attr("href")
            print "    Getting Map Page: ", url
            resp2 = requests.get(url)
            d3 = pq(resp2.content)
            url = d3("[rel='nofollow']:eq(3)").attr("href")
            print "        Getting Map Archive: ", url
            resp3 = requests.get(url)
            file_name = resp3.url.split("?")[0].split("/")[-1]
            f = open("files/%s" % file_name, "w")
            print "        writing to file:", file_name
            sio = StringIO.StringIO(resp3.content)
            f.write(sio.read())
            f.close()
            sio.close()
        except Exception, e:
            print e
    a = d(".pagination a:last")
    if a.html().find("next") == 0:
        get_page(a.attr("href"))


get_page(start_url)
