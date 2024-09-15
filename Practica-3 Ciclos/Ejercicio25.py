"""
a) Escribir un programa que pida al usuario un número n y muestre una línea de n
asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
********

"""
n=int(input("Ingrese un número para n: "))
asteriscos= n* "*"
print(asteriscos)

for i in range(1,n+1):
    print("*",end="")