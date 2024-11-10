#Escribir una función llamada intercambiar que tome una lista de números s y dos enteros positivos a y b menores que la longitud 
#de la lista y cambie el elemento ubicado en s[a] por el elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, 
#sino modificar la que toma como parámetro.

def intercambiar(lista,a,b):
    aux=lista[a]
    lista[a]=lista[b]
    lista[b]=aux
    

numeros=[1,3,5,6,8,99,10]
print("Original    : ", numeros)
intercambiar(numeros,1,5)

print("Intercambiar: ",numeros)