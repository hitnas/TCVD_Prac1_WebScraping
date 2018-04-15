# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:54:57 2018

@author: Santi
"""

import urllib2 
from BeautifulSoup import BeautifulSoup
import csv
from time import strftime
import time 

def saveToCSV (fName, minInfo): 
    with open(fName, "a") as f: 
        writer = csv.writer(f)
        writer.writerows(minInfo)
    print minInfo[0]

mins = 0  

minData=[['Nom', 'Valor', '% Dif', 'Max', 'Min', 'Volum', 
         'Efectiu (milers euros)', 'Data', 'Hora']]
fileName = strftime("%Y-%m-%d")+'_ibex35_minuts.csv'  

logFile = open(strftime("%Y-%m-%d")+'_ibex35_minuts_log.txt','a')         

saveToCSV (fileName, minData)
print strftime("%H:%M"), "Arxiu creat"
logFile.write(strftime("%H:%M")+" Arxiu creat")

mercatTancat = False 
mercatObert = False
comptTancatInici = 0 
comptTancatFinal = 0

while mins < 1440 : 

    minData =[]
    
    hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'ca,en-US;q=0.7,en;q=0.3',  'Connection': 'keep-alive'}
                
    req = urllib2.Request('http://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000', headers=hdr) 
    
    #Try to open the url and if don't succeed gets the exception    
    try:
        page = urllib2.urlopen(req) 
    except (urllib2.HTTPError, urllib2.URLError), e:
        print strftime("%H:%M"), "Error en accedir al web"
        logFile.write(strftime("%H:%M"), "Error en accedir al web")
        time.sleep(60)
        mins +=1 
        continue   
    except:
        print strftime("%H:%M"), "Error desconegut"  
        time.sleep(60)
        mins +=1 
        continue  
        
    #Read the content of the page opened and store it in a BeautifulSoup class object 
    content = page.read()
    doc = BeautifulSoup(content)

    taulaIbex = doc.find("table", {"id":("ctl00_Contenido_tblÍndice").decode("utf-8")})
    minIbex =[]
    dadesIbex = taulaIbex.findAll('tr')
    atributsIbex = dadesIbex[1].findAll('td')
    minIbex.append("IBEX 35")
    minIbex.append(atributsIbex[2].getString())    
    minIbex.append(atributsIbex[3].getString())
    minIbex.append(atributsIbex[4].getString())
    minIbex.append(atributsIbex[5].getString())
    minIbex.append("")
    minIbex.append("")
    minIbex.append(atributsIbex[6].getString())
    minIbex.append(atributsIbex[7].getString())
    minData.append(minIbex)
    
    
    taulaValors = doc.find("table", {"id":"ctl00_Contenido_tblAcciones"})
    
    empreses = taulaValors.findAll('tr')
    for empresa in empreses[1:]:
        atributs = empresa.findAll('td')
        minCompany = []
        for atribut in atributs: 
            if atributs.index(atribut) == 0: 
                minCompany.append(atribut.find("a").getString())
            else: 
                minCompany.append(atribut.getString())
        minData.append(minCompany)
    
    if minCompany[8]=='Cierre': 
        mercatTancat = True 
        if mercatObert == False: 
            comptTancatInici +=1 
        else: 
            comptTancatFinal +=1
    else: 
        comptTancatInici +=2 
        mercatTancat = False
        mercatObert = True
        saveToCSV(fileName, minData)
        print strftime("%H:%M"),"Actualitzat", "comptInici", comptTancatInici, "comptFinal", comptTancatFinal        
        logFile.write("\n"+strftime("%H:%M")+"Actualitzat comptInici "+ str(comptTancatInici)+ " comptFinal "+ str(comptTancatFinal))

        
    if comptTancatInici > 1 : 
        if comptTancatFinal < 2: 
            print strftime("%H:%M"), "Mercat tancat", "comptInici", comptTancatInici, "comptFinal", comptTancatFinal
            logFile.write("\n"+strftime("%H:%M")+" Mercat tancat comptInici "+str(comptTancatInici)+" comptFinal "+str(comptTancatFinal))            
            time.sleep(60)
            mins +=1
            continue       
        else: 
            print strftime("%H:%M"), "Arxiu tancat", "comptInici", comptTancatInici, "comptFinal", comptTancatFinal
            logFile.write("\n"+strftime("%H:%M")+ "Arxiu tancat"+ "comptInici"+str(comptTancatInici)+ "comptFinal"+ str(comptTancatFinal))
            break 
    else: 
        saveToCSV(fileName, minData)    
        time.sleep(60)
        mins +=1 
        print strftime("%H:%M"),"Actualitzat", "comptInici", comptTancatInici, "comptFinal", comptTancatFinal        
        logFile.write("\n"+strftime("%H:%M")+"Actualitzat"+ "comptInici"+ str(comptTancatInici)+ "comptFinal"+ str(comptTancatFinal))

print strftime("%H:%M"), "Arxiu tancat", "comptInici", comptTancatInici, "comptFinal", comptTancatFinal
logFile.write("\n"+strftime("%H:%M")+ " Arxiu tancat "+ " comptInici "+ str(comptTancatInici)+ " comptFinal "+ str(comptTancatFinal))   
logFile.close()