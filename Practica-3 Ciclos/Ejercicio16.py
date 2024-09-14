"""
El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
1 - 1/2 + 1/3 - 1/4 + 1/5

a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
que muestre la aproximación de ln(2) con esa cantidad de términos.

"""

terminos=int(input("Ingrese la cantidad de terminos a sumar: "))
suma=0
for i in range(1,terminos+1):
    suma+= (-1)**(i+1)/i # (-1)**(n+1) / n
    print(suma)

