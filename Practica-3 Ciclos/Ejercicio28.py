"""
Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de
esa letra

"""
palabra=input("Ingrese una palabra: ")
letra=input("Ingrese una letra: ")

apariciones=0
for char in palabra:
    if char==letra:
        apariciones+=1
print(f"Cantidad de veces la letra {letra}: {apariciones}")


