"""
Escribir un programa que pida al usuario un número n y muestre n líneas de 2n - 1
asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
*
***
*****
*******
*********

"""

n=int(input("Ingrese un número n: "))

for i in range(1,n+1):
    asterisco= (2*i-1)*"*" # Genera X cantidad de "*".
    print(asterisco)