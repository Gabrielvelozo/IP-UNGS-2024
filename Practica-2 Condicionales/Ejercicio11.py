"""
Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
mayor que el segundo o viceversa.
"""
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un segundo numero: "))
if num1>num2: print(f"El primero: {num1} es MAYOR  que el segundo {num2}")
elif num2>num1: print(f"El segundo: {num2} es MAYOR  que el primero {num1}")
else: print("son iguales")