#Hacer una función que tome una lista de números decimales y devuelva el promedio de los elementos.

def promedio(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]  
    return suma/len(lista)

numeros=[10,10,1,5]
print(promedio(numeros))