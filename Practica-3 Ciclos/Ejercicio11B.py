"""
b) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla todos los divisores pares de n
"""
n=int(input("ingrese un número n > 0: "))

if n<0: print("El numero debe ser positivo. Vuelva a ingreasar un número.")
else:
    for i in range(1,n+1):
         if n%i==0 and i%2==0:
            print(f"{i}",end=" ")

