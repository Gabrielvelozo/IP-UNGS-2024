#escribir una función q tome como parámetros una cadena y una letra, y retorne la cantidad de veces que aparece esa letra en esa cadena.

def letraRepetida(cadena,letra):
    cantidad=0
    for char in cadena:
        if letra==char:
            cantidad+=1
    return cantidad
    
print(letraRepetida("hoola","o"))