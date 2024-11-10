#Definir función llamada interseccion q tome dos listas sn repetidos y devuelva una nueva lista q contenga sólamente 
#aquellos elementos q estén ambas listas.

def interseccion(lista1,lista2):
    interseccionListas=[]
    for elem in lista1:
        if elem in lista2:
            interseccionListas.append(elem)
    return interseccionListas

num1=[1,2,3,4]
num2=[2,5,6,8]
print(interseccion(num1,num2))