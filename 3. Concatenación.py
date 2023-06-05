# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:37:02 2023

@author: KN_AN
"""

str1="Cisco"
str2="Networking"
str3="Academy"
space=" "

#La concatenación unicamente se utiliza para strings

print(str1+str2+space+str3)
print(str1+str2+str3) #Concatena los datos
print(str1,str2,str3) #Nos ayuda a crear espacio entre los datos


x=5
print(type(x))
print("El valor de x es:",x)
print("El valor de x es: "+str(x))
x=str(x)
print(type(x))