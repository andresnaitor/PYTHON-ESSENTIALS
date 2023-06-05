# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:50:21 2023

@author: KN_AN
"""



listaR=[]
listaS=[]
listaV=[]
lista =["R1","R2","R3",
        "R4","S1","S2","S3",
        "r5","AP1"]

print(len(lista))
for item in lista:
    if "R" in item:
        listaR.append(item)
        #print(item)
        print(listaR)
    elif "S" in item:
        listaS.append(item)
    else:
        listaV.append(item)
        
        