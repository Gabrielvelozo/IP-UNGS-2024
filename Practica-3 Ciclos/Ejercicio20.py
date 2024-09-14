"""
a) Escribir un programa que permita al usuario elegir un número m y un n y muestre
todos los pares de numeros que se pueden formar con los números que están entre
ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberá mostrar
4 4
4 5
4 6
5 4
5 5
5 6
6 4
6 5
6 6

"""

m=int(input("Ingresar un numero m: "))
n=int(input("Ingresar un numero n: "))

for i in range(m,n+1): # i=4 | j=4, j=5, j=6 hasta i=6.
    for j in range(m,n+1):
        print(i,j)