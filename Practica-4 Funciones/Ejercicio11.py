#a) Hacer una función que sume los divisores propios de un número.

def sumaDivisores(x):
    suma=0
    for i in range(1,x):
        if x%i==0:
            suma+=i
    return suma

#print(sumaDivisores(10))

#b)Hacer una función que indique si un número es perfecto. Número perfecto: a es perfecto si la suma de sus divisores propios es igual a a.

def numeroPerfecto(x):
    suma=0
    for i in range(1,x):
        if x%i==0:
            suma+=i
    
    if x==suma: return True
    else: return False

#print(numeroPerfecto(8))

#c) Hacer una función q determine si un número ingresado x el usuario es un número abundante.Número abundante: todo número natural q cumple
# la suma d sus divisores propios es > q el propio número. ej, 12 es abundante ya q sus divisores son 1, 2, 3, 4 y 6 y se cumple q 1+2+3+4+6=16, 
# que es mayor al propio 12.

def numeroAbundante(x):
    suma=0
    for i in range(1,x):
        if x%i==0:
            suma+=i
    if suma>x:
        return "Es abundante" 
    else: 
        return "No es abundante" 

print(numeroAbundante(12))