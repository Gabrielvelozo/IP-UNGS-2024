"""
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
7 (4, 5, 6 y 7).
"""
for i in range(4,8):
    print(i,end=" ")

print("\n")

i=4
while i<=7:
    print(f"{i}",end=" ")
    i+=1

print("\n")

""""
b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¿Qué pasa
si n es menor que m?

"""
m=int(input("Ingrese un número m: "))
n=int(input("Ingrese un número n: "))

for i in range(m,n+1):
    print(i,end=" ")

print("\n")

i=m # ASIGNAMOS m A i PARA NO PERDER EL DATO INGRESADO POR EL USUARIO.
while i<=n:
    print(f"{i}",end=" ")
    i+=1
# SI n ES MENOR QUE m NO ENTRA NUNCA AL CICLO.
