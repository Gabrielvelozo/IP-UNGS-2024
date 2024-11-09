"""
 d) una función que se llame quitarRepeticiones que tome dos parámetros, una
 cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las
 repeticiones de esa letra. Por ejemplo, un programa que llame a la función
 así: quitarRepeticiones(mate cocido, c), deberá retornar la cadena mate
 coido.
"""

def quitarRepeticiones(cadena,letra):
    cadenaNueva=""
    cont=0
    for char in cadena:
        if char==letra and cont==0:
            cadenaNueva+=char
            cont+=1

        if char !=letra:
            cadenaNueva+=char
    return cadenaNueva
        



palabra=input("Ingrese una palabra: ")
letra=input("ingrese una letra: ")
print(quitarRepeticiones(palabra,letra))