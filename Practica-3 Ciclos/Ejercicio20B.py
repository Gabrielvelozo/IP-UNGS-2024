"""
b) Cambiar el programa para que use sólo un ciclo en vez de dos.
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

i=m
j=m

while j<n+1:
    print(j,i)
    i+=1
    if i>n:
        i=m
        j+=1
    
