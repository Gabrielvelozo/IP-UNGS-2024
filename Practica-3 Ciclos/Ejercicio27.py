"""
Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejemplo,
si la palabra es "Ganaste", el programa debería escribir:
***********
* Ganaste *
***********

"""
palabra=input("Ingrese una palabra: ")
# Agregar " " & * antes y despues de la palabra.
longitud_p=len(palabra)+4
asteriscos= "*"*longitud_p
imprimir="* "+palabra+" *"
print(f"{asteriscos}\n{imprimir}\n{asteriscos}")