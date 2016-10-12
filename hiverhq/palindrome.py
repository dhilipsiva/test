#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: palindrome.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-10-12
"""

text = "IOMKILOLIKTCJIOPLLPO"
palindromes = []
cleaned_palindromes = []

if text == text[::-1]:
    print text

text_len = len(text)
for current_len in range(text_len, 3, -1):
    for i in range(0, text_len - current_len + 1):
        sample_text = text[i:i+current_len]
        if sample_text == sample_text[::-1]:
            palindromes.append(sample_text)


def palindrome_exists(palindrome, cleaned_palindromes):
    for cleaned_palindrome in cleaned_palindromes:
        if palindrome in cleaned_palindrome:
            return True
    return False


for palindrome in palindromes:
    palindrome = palindrome.strip()
    if not palindrome_exists(palindrome, cleaned_palindromes):
        cleaned_palindromes.append(palindrome)


print ",".join(cleaned_palindromes)
