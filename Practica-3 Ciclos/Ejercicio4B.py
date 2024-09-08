"""
b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
2, 5, 8, 11, 14.

"""

m=int(input("Ingrese un número m: "))
n=int(input("Ingrese un número n: "))
i=m
for num in  range(i,n+1,3):
    print(num, end=" ")

print("\n")

while i<=n:
    print(f"{i}",end=" ")
    i+=3
