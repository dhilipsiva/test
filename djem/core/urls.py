#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: urls.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-10-05
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""

"""

from core.views import projects, project, files, file, pages
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    url(r'^projects$', projects),
    url(r'^projects/(?P<project_uuid>%s)$' % settings.UUID_REGEX, project),
    url(r'^files$', files),
    url(r'^files/(?P<file_uuid>%s)$' % settings.UUID_REGEX, file),
    url(r'^pages$', pages),
]
