"""
Hacer una función (no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
 Por ejemplo si la cadena fuera sobrevivir, la función debería imprimir
 **************
 * sobrevivir *
 **************
"""
def cadenaAsteriscos(cadena):
   longitud=len(cadena)+4
   asteriscos="*"*longitud
   cadenaAsteriscos="* "+cadena+" *"
   return (f"{asteriscos}\n{cadenaAsteriscos}\n{asteriscos}")


print(cadenaAsteriscos("SOBREVIVIR"))

