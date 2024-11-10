#Escribir una función llamada maximo que tome una lista de números y devuelva el valor del máximo elemento.

def mayorNumero(listaNumero):
    masGrande=0    
    for elem in listaNumero:
        if elem > masGrande:
            masGrande=elem
    return masGrande


numeros=[1,35,36,90,89,90]
print(mayorNumero(numeros))