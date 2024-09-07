"""
Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
"Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.
"""
num1=float(input("ingrese un valor: "))
num2=float(input("ingrse un 2 valor: "))
promedio= (num1+num2)/2
if promedio >=7: print(f"APROBADO, promedio: {promedio}")
else: print(f"DESAPROBADO, promedio: {promedio}")