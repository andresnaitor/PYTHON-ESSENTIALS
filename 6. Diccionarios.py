# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:07:30 2023

@author: KN_AN
"""

dict1={"nombre":"Andres","Apellido":"Baez","Email":"andres.baez@epn.edu.ec",2:"ID"
       ,True:"Matricula",4.5:"Saldo","notas":[10,9,8,7,5]}

print(dict1)
print(dict1["nombre"])
dict1["S1"]="10.10.0.1"
del dict1["nombre"]
print("R2" in dict1)

print(dict1)
