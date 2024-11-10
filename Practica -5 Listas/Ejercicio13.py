#Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como parametros y devuelva la cantidad 
#de veces que aparece n en s.

def frecuencia(lista,n):
    veces=0
    for i in range(len(lista)):
        if lista[i]==n:
            veces+=1
    return veces
    """for elem in lista:
        if elem==n:
            veces+=1
    return veces"""

numeros=[1,1,2,3,6,5,5,5]
n=4
print(frecuencia(numeros,n))