#a) Escribir una función que reciba como parámetro una cadena y la muestre en pantalla 3 veces

def repetirTresVeces(cadena):
    return (cadena +"\n" )*3
    
#print(repetirTresVeces("MAGA"))

#b) Guardar esta de nición de función en un archivo.
#c) Hacer un programa que le pida al usuario una cadena y que la muestre en pantalla 3 veces utilizando la función de nida anteriormente.

user=input("Ingrese una cadena: ")

print(repetirTresVeces(user))