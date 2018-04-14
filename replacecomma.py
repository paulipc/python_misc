#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Find all postitins for <start> tag in a string
#   Replace commas with dots in between <start> and <end> tags

import re

def replacecomma(row, p, stag, etag, lstag, letag):
    # p on Start:in positio
    # end pitaa loytaa startista eteenpain

    epos=row.find(etag,p)+1
    s=row[0:p]
    b=row[p:epos+letag-1]
    b=b.replace(';','.')
    e=row[epos+letag-1:]

    return s+b+e

def replaceallcommas(row, stag, etag):
    a=row
    pos = [m.start() for m in re.finditer(stag, a)]
    lstag = len(stag)
    letag = len(etag)
    for i in pos:
        b=replacecomma(a, i, stag, etag, lstag, letag)
        a=b

    return a

# main

x = 'dk aokdj Starting adkd a; dkaj Ending ; kdjas Starting adkdjkas Ending adnasdkj Starting dja; ; dalolEnding dkaoskjs'
x=replaceallcommas(x,'Starting','Ending')
print x
