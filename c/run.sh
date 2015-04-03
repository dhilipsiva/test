#! /bin/sh
#
# run.sh
# Copyright (C) 2015 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#


gcc $1 -o $1-out
./$1-out
