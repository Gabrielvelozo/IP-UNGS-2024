#Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b menores que la longitud de la lista y devuelva 
#el índice del máximo elemento considerando solo los que están entre el índice a y el índice b.

def maximoEntre(lista,a,b):
    maximoNumero=lista[a]
    indice=a
    for i in range(a,b+1):
        if lista[i]>maximoNumero:
            maximoNumero=lista[i]
            indice=i
    return indice

numeros=[1,2,3,4,5,6,7,881,9,10,100,12,13,14,15,18]
a=4
b=12
print(maximoEntre(numeros,a,b))