"""
Hacer un programa que solicite dos cadenas, nombre y apellido y arme el legajo de estudiantes
de la universidad de la siguiente manera:
Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
primeras letras del apellido y por ultimo la primera y ultima del nombre.
Por ejemplo:
JavierRodriguez 38946702
Legajo: 389_rodjr

"""
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
dni=input("Ingrese su dni: ")
primera_letra=nombre[0]
ultima_letra=nombre[-1]
tres_apellido=apellido[:3]

legajo=dni[:3]+"_"+tres_apellido+primera_letra+ultima_letra
print("Legajo: ",legajo)