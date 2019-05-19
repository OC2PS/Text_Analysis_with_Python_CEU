#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This example can be found in: Automate the Boring Stuff
"""

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())


#find all numbers in text
mo = phoneNumRegex.findall('My number is 415-555-4242 or 415-555-4243.')


#Grouping with Parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.groups()
areaCode, mainNumber = mo.groups()

print(areaCode)
print(mainNumber)
