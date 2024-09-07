"""
Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
verificar los resutlados.
"""

a=int(input("ingrese un valor para a: "))
b=int(input("Ingrese un valor para b: "))
c=int(input("ingrese un valor para c: "))

if a>=b and a>=c: print(f"EL MAYOR ES: {a}")
elif b>=a and b>=c: print(f"EL MAYOR ES: {b}")
elif c>=a and c>=b: print(f"EL MAYOR ES: {c}")
else: print("DATO NO VALIDO")