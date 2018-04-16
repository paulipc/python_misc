
# coding: utf-8

import re
import json

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


# jaetaan rivit kahteen osaan. eka osa on normi csv:tä ja loput on jsonia. json pitää  konvertoida niin, että kommenttikenttä ei sisällä puolipisteitä, muuten rivi menee poikki kesken kaiken.

kentat=['ytl_etunimet', 'ytl_isexecuted', 'ytl_wholename', 'ytl_lukiokoodi', 'ytl_sukunimi', 'ytl_workflowname', 'ytl_id', 'ytl_taskid', 'description', 'ytl_starttime', 'ytl_recordnumber', 'ytl_taskowner', 'ytl_status', 'ytl_lukionimi', 'ytl_paatospvm', 'ytl_procid', 'ytl_commenthistory']
firstrow = True
i = 1
pos = []
with open('/home/diaari/newdiaaridump.csv') as f:
    for row in f:
        if firstrow:
            firstrow = False
        else:
            pos = [m.start() for m in re.finditer(";", row)]
            #print(pos)
            beg = row[:pos[5]].split(';')
            #print(beg)
            end = row[pos[5]+1:]
            end = replaceallcommas(end,'ytl_commenthistory"":""','"",')
            end = end.replace('"{','{')
            end = end.replace('}"','}')
            end = end.replace('""','"')
            end = json.loads(end)
            pkentat=[]
            pkentat = [item for item in kentat if item not in list(end.keys())]
            for k in pkentat:
                end[k]=''
            #print(end["ytl_commenthistory"])
            end["ytl_commenthistory"] = end["ytl_commenthistory"].replace('\n','')
            print(
            beg[0]+";"+ \
            beg[1]+";"+ \
            beg[2]+";"+ \
            beg[3]+";"+ \
            beg[4]+";"+ \
            beg[5]+";"+ \
            end['ytl_etunimet']+";"+ \
            end['ytl_isexecuted']+";"+ \
            end['ytl_wholename']+";"+ \
            end['ytl_lukiokoodi']+";"+ \
            end['ytl_sukunimi']+";"+ \
            end['ytl_workflowname']+";"+ \
            end['ytl_id']+";"+ \
            end['ytl_taskid']+";"+ \
            end['description']+";"+ \
            end['ytl_starttime']+";"+ \
            end['ytl_recordnumber']+";"+ \
            end['ytl_taskowner']+";"+ \
            end['ytl_status']+";"+ \
            end['ytl_lukionimi']+";"+ \
            end['ytl_paatospvm']+";"+ \
            end['ytl_commenthistory']+";"+ \
            end['ytl_procid'])
