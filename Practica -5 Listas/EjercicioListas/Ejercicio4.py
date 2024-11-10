#4- Hacer una función que reciba una lista y devuelva otra solo con los elementos sin repeticiones.
def cuantasVeces(num,lista):
    cont=0
    for elemento in lista:
        if elemento ==num:
            cont+=1
    return cont

numeros=[1,2,3,3,4,5,6,8]
nueva=[]
for elemen in numeros:
    if not cuantasVeces(elemen,nueva):
        nueva.append(elemen)
   
  


print(nueva)
