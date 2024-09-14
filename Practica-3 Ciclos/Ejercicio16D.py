"""
El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
1 - 1/2 + 1/3 - 1/4 + 1/5
d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
pida al usuario un número decimal e (muy chico) y calcule la suma hasta que el
error comparado con el valor de la calculadora sea menor que e

"""
e=float(input("Ingrese un número decimal muy chico: "))
import math
suma=0
i=1
while abs(math.log(2)-suma)>e:
    suma+= (-1)**(i+1)/i
    i+=1
print(f"la cantidad de terminos hasta el N ingresado {e}, es : {i-1}")

