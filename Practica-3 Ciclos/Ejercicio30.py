"""
Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
"programador"
"r"
el programa debe devolver "p * og * amado*"

"""
cadena=input("Ingrese una palabra: ")
letra=input("Ingrese una letra: ")
# Nueva cadena, para intercambiar los caracteres por "*"
nueva_cadena=""
for char in cadena:
    if char==letra:
        nueva_cadena+="*"
    else:
        nueva_cadena+=char

print(nueva_cadena)        
