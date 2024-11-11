#Escribir un programa que pida al usuario una cadena, y luego escriba en pantalla la cantidad de veces que aparece cada letra 
# (sin mostrar las que no aparecen).

cadena="conocido"
alfabeto="abcdefghijklmnñopqrstuvwxyz"
def cuantasVeces(cadena,letraBuscar):
    cont=0
    for letra in cadena:
        if letra == letraBuscar:
            cont+=1
    return cont

for letra in alfabeto:
    cantidad=cuantasVeces(cadena,letra)
    if cantidad>=1:
        print(letra,":",cantidad)
    

