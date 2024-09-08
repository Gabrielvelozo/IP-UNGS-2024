"""
c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
el programa deberá mostrar 2, 6, 10, 14.
"""

n=int(input("ingrese un número n: "))
m=int(input("ingrese un número m: "))
p=int(input("ingrese un número p: "))
i=n

"""while i<=m:
    print(f"{i}",end=" ")
    i+=p"""

print("\n***************\n")

for num in range(i,m+1,p):
    print(num,end=" ")
