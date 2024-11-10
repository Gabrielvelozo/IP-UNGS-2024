#Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de ese entero

def divisores(numero):
    listaDiviores=[]
    for elem in range(1,numero+1):
        if numero%elem==0:
            listaDiviores.append(elem)
    return listaDiviores

print(divisores(12))
