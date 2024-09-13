"""
Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
faltantes las reemplazará por "*". Ejemplos:
clemente CLMN
rivera RVR*
oreo R***
La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
Ejemplos: CLMN1 RVR*4 R***7

"""
import random # Importar libreria.
apellido= input("Ingrese su apellido: ")
consonantes="" # Agrupar constantes.

for char in apellido:

    if not char in  "aeiou" and len(consonantes)<4: # Mientras no sea vocal y menor a 4.
        consonantes+=char

while len(consonantes)<4: # Si es menor a 4, agregar "*".
    consonantes+="*"

clave=consonantes+str(random.randrange(10)) # Sumar un numero random de 0,9.
print(clave)
    


