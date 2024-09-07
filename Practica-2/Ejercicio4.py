"""
a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
Python y por último correr el programa con los valores iniciales de las corridas y
verificar que funciona como se esperaba.
b) Ídem anterior pero para encontrar el menor
"""
a=int(input("Ingrese un numero para a: "))
b=int(input("Ingrese un numero para b: "))

if a>b: print(f"EL MAYOR ES a: {a}")
elif b>a:print(f"EL MAYOR ES b: {b}")
else:print("SON IGUALES")

if a<b: print(f"EL MEMOR ES a: {a}")
elif b<a:print(f"EL MENOR ES b: {b}")
else:print("SON IGUALES")