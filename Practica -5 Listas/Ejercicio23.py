#Modificar el programa del ejercicio 1.2 para que muestre visualmente los resultados, repitiendo asteriscos

palabra="conocido"
alfabeto="abcdefghijklmnñopqrstuvwxyz"

def cuantasVeces(cadena,letra_encontrar):
    cant=0
    for letra in cadena:
        if letra==letra_encontrar:
            cant+=1
    return cant

for letra in alfabeto:
    cantidad=cuantasVeces(palabra,letra)
    if cantidad>=1:
        print(letra,":",cantidad*"*")

