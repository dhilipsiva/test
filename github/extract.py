#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: extract.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-04-21
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""
487e792be5d0c0ef91ea6bf80859569f35dbe3a4
"""

import requests
import json

repos = []
url_file = open("urls.txt", "r")
repo_file = open("repo.json", "w")

for line in url_file.readlines():
    url = "https://api.github.com/repos/%s" % line.replace("\n", "")
    print url
    r = requests.get(url, auth=(
        "487e792be5d0c0ef91ea6bf80859569f35dbe3a4", "x-oauth-basic")
    )
    _json = r.json()
    print _json
    repos.append(_json)
repo_file.write(json.dumps(repos))


print repos

repo_file.close()
url_file.close()
