import urllib.request as ur
import lxml.html
from statistics import stdev
import numpy

def getDevLst(day,dayBefore):
    fDay = float(day[4])
    fDayBefore = float(dayBefore[4])

    dev = ((fDay - fDayBefore)/fDayBefore)*100
    return (dev)

def getIndex(curr):
    index = 0.0
    unit = 3.44
    days = 29

    try:
        data = ur.urlopen('https://coinmarketcap.com/currencies/'+curr+'/historical-data/').read()
        tree = lxml.html.fromstring(data)
    except:
        return None


    tables = []
    for tbl in tree.iterfind('.//table'):
        tele = []
        tables.append(tele)
        for tr in tbl.iterfind('.//tr'):
            text = [e.strip() for e in tr.xpath('.//text()') if len(e.strip()) > 0]
            tele.append(text)

    tables = tables[0]
    deviationLst = []
    for i in range(1,len(tables)-1):
        deviationLst.append(getDevLst(tables[i],tables[i+1]))

    dev = stdev(deviationLst)

    finalDev = float((days**.5)*dev)

    return ('%.2f' % finalDev)
