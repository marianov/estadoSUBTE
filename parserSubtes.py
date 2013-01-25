#!/usr/bin/env python
# coding: utf-8
import urllib2
import urllib
from re import sub
u=urllib2.urlopen("http://www.metrovias.com.ar/V2/InfoSubteSplash.asp")
lines=u.readlines()
estadosLine =lines[24]
estados = sub("<\/?b>","", estadosLine.decode("latin-1").replace("&nbsp;","") ).split(";")[0:7] 
estados = [ e.split("'")[1] for e in estados ]
for e in estados:
  print e.encode("latin-1")
