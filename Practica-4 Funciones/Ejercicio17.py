#Escribir una función (y probarla en un programa) para cada una de las siguientes descripciones:

"""
 b) una función que se llame aparece que tome dos parámetros, una letra y una cadena,
 y devuelva True si la letra aparece en la cadena y False en caso contrario.
"""

def aparece(cadena,letra):
    for char in cadena:
        if char==letra:
            return True
    return False

"""
 a) una función que se llame tieneRepetidas que tome una cadena como parámetro y
 devuelva True si esa cadena tiene alguna letra que aparece más de una vez y False
 en caso contrario
"""
def cantRepetida(cadena,letra):
    contador=0
    for char in cadena:
        if char==letra:
            contador+=1
    return contador

def tieneRepetidas(cadena):
    for char in cadena:
        if cantRepetida(cadena,char)>1:
            return True
    return False

        
#c) una función que se llame dameRepetida que tome una cadena como parámetro y retorne la primer letra que aparece repetida en la cadena

def dameRepetida(cadena):
    for char in cadena:
        if cantRepetida(cadena,char)>1:
            return char
    return "No tiene repetidas"
    




palabra=input("Ingrese una palabra: ")

print(dameRepetida(palabra))
