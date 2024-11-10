#2- Hacer una función que dado un entero y una lista de enteros indique cuantas veces aparece el entero en la lista.

def cuantasVeces(lista,num):
    cont=0
    for elemento in lista:
        if elemento ==num:
            cont+=1
    return cont

entero=87
listaEntero=[33,15,-2,87,87,87]
print(cuantasVeces(listaEntero,entero))