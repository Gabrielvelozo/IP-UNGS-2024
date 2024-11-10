#Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista que contenga 
#los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos.

def union(listaA,listaB):
    listaSinRepetidos=[]
    for elemento in listaA:
        listaSinRepetidos.append(elemento)

    for elemento in listaB:
        if elemento not in listaSinRepetidos:
            listaSinRepetidos.append(elemento) 
    return listaSinRepetidos

numA=[1,3,5,7]
numB=[2,4,6,8]

print(union(numA,numB))