#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

# Settings


AWS_SECRET_KEY = 'secret_key'
AWS_ACCESS_KEY = 'access_key'
AWS_BUCKET = 'bucket'
AWS_BASE_URL = 'https://*.cloudfront.net'
AWS_EXPIRY_TIME = 60 * 30  # Half an hour
AWS_FORCE_HTTP = True
UPLOAD_TO_S3 = False
MEDIA_URL = ""

"""
A Wrapper around boto to upload to s3
"""
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from django.conf import settings

if settings.UPLOAD_TO_S3:
    conn = S3Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
    bucket = conn.get_bucket(settings.AWS_BUCKET)


def key_for_file(file):
    """
    docstring for key_for_file
    """
    return '/files/' + file._file.path.split('media/')[1]


def upload(file):
    k = Key(bucket)
    k.key = key_for_file(file)
    k.set_contents_from_filename(file._file.path)


def temp_url(file):
    """
    Function to generate a temproary AWS URL for fiven file object
    """
    k = Key(bucket)
    k.key = key_for_file(file)
    return k.generate_url(
        expires_in=settings.AWS_EXPIRY_TIME,
        force_http=settings.AWS_FORCE_HTTP)


def process_file(file):
    """
    Upload the file to s3
    """
    if not settings.UPLOAD_TO_S3:
        return file
    try:
        if not file.uploaded:
            upload(file)
            os.remove(file._file.path)
            file.uploaded = True
            file.save()
    except Exception:
        print "unable to upload file to s3"
    finally:
        return file

"""
Model configuration
"""
from django.db import models

AWS_PREFIX = AWS_BASE_URL + MEDIA_URL


class Model:

    uploaded = models.BooleanField(default=False)

    def get_url(self, size=""):
        if self.uploaded:
            filename, extension = self._file.name.rsplit('.', 1)
            path = AWS_PREFIX + filename
        else:
            filename, extension = self._file.url.rsplit('.', 1)
            path = filename
        if size:
            path += "-" + size
        path += "." + extension
        return path

    @property
    def url(self):
        if self.uploaded:
            return temp_url(self)
        return self._file.url
