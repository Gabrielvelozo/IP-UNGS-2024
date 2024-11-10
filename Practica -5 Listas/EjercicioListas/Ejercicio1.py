#1- Hacer una función que recibe una lista y un entero e indique si el entero está en la lista.

def estaNumero(lista,numero):
    for elemento in lista:
        if elemento ==numero:
            return True
    return False

numeroLista=[12,4,-8,22]
num=20 
print(estaNumero(numeroLista,num))