#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: docker.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-01-19
"""

from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
from io import StringIO
from docker import Client
dockerfile = u'''
# Shared Volume
FROM busybox:buildroot-2014.02
MAINTAINER dhilipsiva, dhilipsiva@gmail.com
VOLUME /data
CMD ["/bin/sh"]
'''
f = StringIO(dockerfile)
cli = Client(base_url='tcp://192.168.99.100:2375')
response = [line for line in cli.build(
    fileobj=f, rm=True, tag='dhilipsiva/volume'
    )]
print(response)
