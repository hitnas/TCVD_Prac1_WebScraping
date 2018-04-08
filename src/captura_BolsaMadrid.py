# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:54:57 2018

@author: Santi
"""

import urllib2 
from BeautifulSoup import BeautifulSoup
import csv
from bson.json_util import loads
import json 

from time import time, strftime
import zipfile
import ftplib 

dayData =[]

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'ca,en-US;q=0.7,en;q=0.3',  'Connection': 'keep-alive'}
#req = urllib2.Request('http://www.meteo.cat/observacions/xom_observacio', headers=hdr) 
#
##Try to open the url and if don't succeed gets the exception    
#try:
#    page = urllib2.urlopen(req) 
#except urllib2.HTTPError, e:
#    print e.fp.read()
#        #Read the content of the page opened and store it in a BeautifulSoup class object 
#content = page.read()
#doc = BeautifulSoup(content)
##print doc
#i=1
#y=1
#script = doc.findAll("script")
#for docs in script :
#    pos1 = docs.text.find("Meteocat.cercadorMunicipi")
#    if pos1 > 0: 
#        pos2 = docs.text[pos1:].find("]);")+pos1
#        munis =  docs.text[pos1+27:pos2+1]
#        npos1=0
#        npos2=0
#        i =0
#        print len(munis)
#        while len(munis)>10: 
#            i +=1
#            npos1 = munis.find('{"codi":"')
#            npos2 = munis.find('}}')+2
##            print i, munis[npos1:npos2]
#            item = loads(munis[npos1:npos2])
##            coord = loads(item["coordenades"])
#            print item["codi"], item["variables"], item["nom"], item["slug"],item["coordenades"]["latitud"], item["coordenades"]["longitud"], item["comarca"]["codi"], item["comarca"]["nom"]
#            munis = munis[npos2:]
            
            
req = urllib2.Request('http://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000', headers=hdr) 

#Try to open the url and if don't succeed gets the exception    
try:
    page = urllib2.urlopen(req) 
except urllib2.HTTPError, e:
    print e.fp.read()
        #Read the content of the page opened and store it in a BeautifulSoup class object 
content = page.read()
doc = BeautifulSoup(content)
#print doc

#i=1
#y=1
taulaValors = doc.find("table", {"id":"ctl00_Contenido_tblAcciones"})

empreses = taulaValors.findAll('tr')
for empresa in empreses:
    atributs = empresa.findAll('td')
    dayCompany = []
    for atribut in atributs: 
        if atributs.index(atribut) == 0: 
            dayCompany.append(atribut.find("a").getString())
        else: 
            dayCompany.append(atribut.getString())
    dayData.append(dayCompany)
        
with open("test.csv", "a") as f: 
    writer = csv.writer(f)
    writer.writerows(dayData)

#    cols = [ele.text.strip() for a in atributs]
#    data.append([ele for ele in cols if ele])

#print taulaValors
#links = taulaValors.findAll("a")
#for link in links: 
#    print link.getString()
#script = doc.find("div", "estacions") 
#for docs in script :
#    packages = itembox.findAll("div", "cigarbuybtn left")
#    
#    itembox.find("a", "title cblack oswald").getString()#.strip()
#    pos1 = docs.text.find("Meteocat.cercadorMunicipi")
#    if pos1 > 0: 
#        pos2 = docs.text[pos1:].find("]);")+pos1
#        munis =  docs.text[pos1+27:pos2+1]
#        npos1=0
#        npos2=0
#        i =0
#        print len(munis)
#        while len(munis)>10: 
#            i +=1
#            npos1 = munis.find('{"codi":"')
#            npos2 = munis.find('}}')+2
##            print i, munis[npos1:npos2]
#            item = loads(munis[npos1:npos2])
##            coord = loads(item["coordenades"])
#            print item["codi"], item["variables"], item["nom"], item["slug"],item["coordenades"]["latitud"], item["coordenades"]["longitud"], item["comarca"]["codi"], item["comarca"]["nom"]
#            munis = munis[npos2:]
##        print munis[:20]
#        npos1 = munis.find('{"codi":"')
#        npos2 = munis.find('}}')
#        print npos1, npos2, munis[npos1+1:npos2]
#        munis = munis[npos2:]
#        print munis[:20]
#        
#        items = json.loads(docs.text[pos1+27:pos2+1])
#        for item in items: 
#            print item 
#            y +=1

#    if docs.text.startswith('$(document).ready(function ()'): 
#        print docs.text[:200]
#        i +=1
#Meteocat.cercadorMunicipi
#        pos1 = docs.text.find("{")
#        pos2 = docs.text.rfind("}")
#        items = loads(docs.text[pos1-1:pos2+2])
#        for item in items : 
#            print item
#            print y
#            y +=1
#    else: 
#        print docs.text[:200]
#        i +=1
##            item['imgUrl'] = imgUrl
##            item['date'] = dataConsulta
##            item['web'] = "CigarsInt"
##            prodLinks = doc.findAll("a", "title")
##            prodId = item["ProductId"]
##            item['link'] = ""
##            for prod in prodLinks : 
##                if str(prodId) in str(prod) : 
##                    item['link'] = "http://www.cigarsinternational.com"+prod.get("href")
##                    item['currentUrl'] = currentUrl                        
##            webData.append(item)
##            
##            
#{"codi":"250019",
#"variables":null,
#"nom":"Abella de la Conca",
#"slug":null,
#"coordenades":{
#    "latitud":42.161303653992505,
#    "longitud":1.0917273756684647},
#"comarca":{
#    "codi":25,
#    "nom":"Pallars Jussà"
#    }
#}