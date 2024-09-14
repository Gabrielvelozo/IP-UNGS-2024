"""
b) Cambiar el programa para que use sólo un ciclo en vez de dos
"""
m=int(input("Ingresar un numero m: "))
n=int(input("Ingresar un numero n: "))

i=m
j=m

while j<n+1: # Mientras J sea menor a 7 ingresa al cliclo.
    print(j,i)
    i+=1 # No entra al if hasta valer 7.
    if i>n:
        j+=1 # Incrementa a J en 5 y 6.
        i=j 