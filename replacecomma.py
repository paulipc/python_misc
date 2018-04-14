#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Find all postitins for <start> tag in a string
#   Replace commas with dots in between <start> and <end> tags

import re

def replacecomma(row,p):
    # p on Start:in positio
    # end pitaa loytaa startista eteenpain
    epos=row.find('End',p)+1
    s=row[0:p]
    b=row[p:epos+2]
    b=b.replace(';','.')
    e=row[epos+2:]

    return s+b+e

def replaceallcommas(row):
    a=row
    pos = [m.start() for m in re.finditer('Start', a)]

    for i in pos:
        b=replacecomma(a,i)
        a=b

    return a

# main

x = 'dk aokdj Start adkd a; dkaj End ; kdjas Start adkdjkas End adnasdkj Start dja; ; dalolEnd dkaoskjs'
x=replaceallcommas(x)
print x