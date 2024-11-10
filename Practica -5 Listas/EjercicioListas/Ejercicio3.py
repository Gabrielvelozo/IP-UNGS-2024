#3- Hacer una función que reciba una lista de enteros y devuelva el máximo.

def maximo(listaNumero):
    maximo=0    
    for elem in listaNumero:
        if elem > maximo:
            maximo=elem
    return maximo


numeros=[1,35,36,90,89,90]
print(maximo(numeros))
