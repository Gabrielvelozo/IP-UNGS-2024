"""
b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
16 32
"""
n=int(input("Ingrese un número > a 0: "))

for i in range(n):
    print(f"{2**i}",end=" ")
