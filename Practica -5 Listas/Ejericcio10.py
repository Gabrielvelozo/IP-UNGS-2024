#Escribir una función llamada maximoIndice que tome una lista de números y devuelva el índice del máximo elemento.

def maximoIndice(lista):
    mayorNumero=lista[0]
    indice=0
    for i in range(1,len(lista)):
        if lista[i]>mayorNumero:
            mayorNumero=lista[i]
            indice=i

    return indice

numeros=[1,2,3,5,8,955,4]
print(maximoIndice(numeros))