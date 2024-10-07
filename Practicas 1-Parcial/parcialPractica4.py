#Hacer un sistema que genere una cadena que tenga los 2 primeros caracteres del dni luego un "*",despues los dos ultimos
# caracteres del nombre, luego un "_" y por ultimo  el primer y ultimo  caracter del apellido.

nombre=input("Nombre: ")
apellido=input("Apellido: ")
dni=input("dni: ")

cadena=""
for char in dni:
    if len(cadena)<2:
        cadena+=char
cadena+="*"

contador=0
for char in nombre:
    if contador==len(nombre)-2 or contador==len(nombre)-1:
        cadena+=char
    contador+=1
cadena+="_"

c_apellido=0
for char in apellido:
    if c_apellido==0 or c_apellido==len(apellido)-1:
        cadena+=char
    c_apellido+=1

print(cadena)