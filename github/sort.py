#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: sort.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-04-21
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""

import json
from operator import itemgetter


repo_file = open("repo.json", "r")
url_file = open("urls-sorted.txt", "w")

repos = json.loads(repo_file.read())


new_repos = []

for repo in repos:
    try:
        print "%d - %s" % (repo['subscribers_count'], repo['html_url'])
        new_repos.append(repo)
    except Exception:
        pass

new_repos = sorted(
    new_repos, key=itemgetter('subscribers_count'), reverse=True)

for repo in new_repos:
    print "=========================================================="
    print json.dumps(repo)
    url_file.write("%s - (%d watchers)\n" % (
        repo['html_url'], repo['subscribers_count']))

repo_file.close()
url_file.close()
