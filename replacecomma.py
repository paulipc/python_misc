#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Find all postitins for <start> tag in a string
#   Replace commas with dots in between <start> and <end> tags

import re

def replacecomma(row, p, etag, letag):
    # p on Start:in positio
    # end pitaa loytaa startista eteenpain

    epos=row.find(etag,p)+1
    s=row[0:p]
    b=row[p:epos+letag-1]
    b=b.replace(';','.')
    e=row[epos+letag-1:]

    return s+b+e

def replaceallcommas(row, stag, etag):
    pos = [m.start() for m in re.finditer(stag, row)]
    letag = len(etag)
    for i in pos:
        row=replacecomma(row, i, etag, letag)

    return row

# main

x = 'dk aokdj Starting adkd a; dkaj Ending ; kdjas Starting adkdjkas Ending adnasdkj Starting dja; ; dalolEnding dkaoskjs'
x=replaceallcommas(x,'Starting','Ending')
print x
