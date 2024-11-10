#Definir una función llamada diferencia que tome dos listas sin repetidos y devuelva una nueva lista que 
#contenga los elementos la primera que no estén en la segunda

def diferencia(listaA,listaB):
    listaSnRepetidos=[]
    for elemento in listaA:
        if elemento not in listaB:
            listaSnRepetidos.append(elemento)
    return listaSnRepetidos

numA=[1,5,3]
numB=[4,5,6]
print(diferencia(numA,numB))