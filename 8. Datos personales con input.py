# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:24:48 2023

@author: KN_AN
"""

print("Datos personales para la obtención de la cedula de ciudadania")

nombre=input("Ingrese su primer nombre: ")
apellido=input("Ingrese su primer apellido: ")
location=input("Ingrese el sector donde vive:")
edad=int(input("Ingrese su edad: "))
if edad <10:
    print("infante")
elif edad >= 10 and edad <= 20:
    print("adolescente")
else:
    print("adulto")
print(nombre)
print(apellido)
print(location)
print(edad)
