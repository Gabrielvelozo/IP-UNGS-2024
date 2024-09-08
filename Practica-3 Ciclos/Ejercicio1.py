"""
a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales (1, 2, 3, 4 y 5)
"""
for i in range(1,6):
    print(i,end=" ")

print("\n")

i=1
while i<=5:
    print(f"{i}",end=" ")
    i+=1

print("\n")

"""
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
primeros n números naturales (1, 2, · · · , n).
"""
n=int(input("Ingrese un número: "))

for i in range(1,n+1):
    print(i,end=" ")

print("\n")

i=1
while i<=n:
    # END " " PARA PONERLOS DE LADO.
    print(f"{i}",end=" ")
    i+=1