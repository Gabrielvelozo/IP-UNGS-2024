#4- Hacer una función que reciba una lista y devuelva otra solo con los elementos sin repeticiones.

def cuantasVeces(num,lista):
    cont=0
    for elemento in lista:
        if elemento ==num:
            cont+=1
    return cont
listaNum=[1,1,2,3,5,5,6,8,8,9]
nueva=[]
for elem in listaNum:
    if cuantasVeces(elem,listaNum)==1:
        nueva.append(elem)
print(nueva)