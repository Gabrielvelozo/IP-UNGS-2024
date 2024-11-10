#Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido, y False en caso contrario.

def tieneRepetidos(lista):
    
    for i in range(len(lista)):
        if lista[i] in lista[i+1]:
            return True
    return False

lista=[2,3,7,6,78,7]
print(tieneRepetidos(lista))