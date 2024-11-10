"""Hacer un programa que guarde la siguiente lista en una variable: [elefante, jirafa,
 mono], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
 cuarto animal de la lista."""

animales= ["elefante","jirafa","mono"]
nuevoAnimal=input("Ingrese un animal: ")
animales.append(nuevoAnimal)

print(animales[3])  
