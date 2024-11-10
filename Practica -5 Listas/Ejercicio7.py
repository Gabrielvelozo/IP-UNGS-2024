#Definir una función llamada dondeAparece q tome una lista de enteros y un entero llamado blanco como parámetros, y devuelva el primer índice
#donde blanco aparece en el arreglo, si lo hace, y-1 en caso contrario.

def dondeAparece(lista,blanco):
    for i in range(len(lista)):
        if lista[i]==blanco:
            return i
    return -1
    """for elem in lista:
        if elem==blanco:
            return elem
    return -1"""

numeros=[1,1,33,12,5,-4,4]
blanco=33
print(dondeAparece(numeros,blanco))
