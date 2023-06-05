# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:52:01 2023

@author: KN_AN
"""

lista=["R1",2.566,5,True,False]
print(lista)
print(lista[0])
print(lista[-1])


tupla=("R1",2.566,5,True,False)
print(tupla[0])

lista[4]="AP1" #nO SE PUEDE CAMBIAR LOS DATOS DE LAS TUPLAS
del lista[4]

print(tupla)
print(lista)
