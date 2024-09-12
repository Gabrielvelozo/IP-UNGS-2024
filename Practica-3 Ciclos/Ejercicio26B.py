"""
b) Hacer una programa que, dada una palabra, la escriba pegada a la derecha de la
pantalla

"""
ancho_pantalla=80
palabra=input("ingrese una palabra: ")
largo_palabra=len(palabra)

derecha=ancho_pantalla-largo_palabra
imprimir=derecha * " " + palabra
print(imprimir)