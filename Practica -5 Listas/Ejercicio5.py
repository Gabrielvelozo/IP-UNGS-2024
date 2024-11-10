"""Definir una función llamada sonFactores que tome un entero n y una lista de enteros, y devuelva True si los números 
de la lista son factores de n (es decir, si n es divisible por todos ellos)
"""

def sonFactores(lista,entero):
    
    for numero in lista:
        if numero%entero!=0:
            return False
    return True
   

enteros=[2,4,6,8,10]
n=1
print(sonFactores(enteros,n))