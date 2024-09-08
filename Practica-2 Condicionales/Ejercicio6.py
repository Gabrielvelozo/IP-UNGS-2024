"""
Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
y muestre por pantalla "Usted ingresó un número de una sola cifra" o "Usted ingresó un número
de más de una cifra" según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
y luego correrlo en la computadora con los valores iniciales de las corridas y verificar que hayan
dado como se esperaba
"""

num=int(input("Ingrese un numero entero: "))
if num>0 and num<10: print("Ingreso un número de una CIFRA")
elif num>=10 and num<100: print("Ingreso un número de dos CIFRAS")
elif num>=100 and num<1000: print("Ingreso un número de tres CIFRAS")
else: print("DATO INCORRECTO")