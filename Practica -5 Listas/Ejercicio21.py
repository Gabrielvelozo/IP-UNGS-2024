#Definir una función que tome una lista de números s y un número decimal x y cambie todos los elementos menores que x por 0.

def reemplazarMenores(lista,numero):
    listaMenores=[]
    for elemento in lista:
        if elemento < numero:
            listaMenores.append(0)
        else:
            listaMenores.append(elemento)
    return listaMenores

print(reemplazarMenores([1,5,15,5,17,5,3,5,8,7],5))
