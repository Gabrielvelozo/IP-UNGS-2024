#a) Escribir una función con el siguiente encabezado: def exclamar(unaCadena): que retorne la misma cadena entre símbolos de exclamación (½!)
def exclamar(cadena):
    return "¡"+ cadena + "!"

#print(exclamar("MAGA"))

#b) Escribir una función con el siguiente encabezado: def gritar(unaCadena): que retorne la misma cadena entre 3 símbolos de exclamación (½½½!!!)

def gritar (cadena):
    return "¡¡¡"+cadena+"!!!"

#print(gritar("MAGA"))
print(exclamar(exclamar(exclamar("MAGA"))))