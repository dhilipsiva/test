#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: ld.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-07-14
"""

import ldap

base = "ou=Testing,dc=stroeder,dc=de"
scope = ldap.SCOPE_SUBTREE
conn = ldap.initialize('ldap://foo')
conn.simple_bind_s("reset", "P@ssw0rd")
r = conn.search_s(base, scope, '(objectClass=*)')
for dn, entry in r:
    print("DN: ", dn)
    print("Entry", entry)
