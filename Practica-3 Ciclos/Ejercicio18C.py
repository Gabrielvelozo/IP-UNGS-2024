"""
c) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
pida al usuario un número decimal e (muy chico) y calcule la suma hasta que el
error comparado con el valor de la calculadora sea menor que e
"""

import math
f=float(input("Ingrese un número decimal muy chico: "))
e=1
factorial=1
i=1
while math.e-e >f:
    factorial *=i
    e += 1/factorial
    print(math.e - e) # Validar si esta bien el buble en cada iteracion.
    i+=1
print(f"A partir del término {i-1}, el valor es menor a {f} : {math.e - e}")

# Luego de poner un numero menor a 0.0000 sale un error.