"""
a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales (1, 2, 3, 4 y 5)
"""
i=1
while i<=5:
    print(f"{i}",end=" ")
    i+=1

"""
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
primeros n números naturales (1, 2, · · · , n).
"""
n=int(input("Ingrese un número: "))

i=1
while i<=n:
    # END " " PARA PONERLOS DE LADO.
    print(f"{i}",end=" ")
    i+=1