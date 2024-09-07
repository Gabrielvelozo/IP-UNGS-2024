"""
Un profesor clasifica las notas de sus alumnos de la siguiente manera:
1-3 Reprobado
4-6 Debe rendir examen final
7-10 Eximido
a) Escribir un programa que indique la clasificación de una nota.
b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
del mismo.
"""

reprobado= (1,3)
final= (4,6)
eximido= (7,10)

nota1=float(input("Ingresa el valor de la primera nota: "))
nota2=float(input("Ingresa el valor de la segunda nota: "))
nota3=float(input("Ingresa el valor de la tercera nota: "))
promedio=(nota1+nota2+nota3)//3

if nota1>=1 and nota1<=3: print(f"REPROBADO, promedio: {promedio}")
elif nota1>=4 and nota1<=6: print(f"FINAL, promedio: {promedio}")
elif nota1>=7 and nota1<=10: print(f"EXIMIDO, promedio: {promedio}")
else: print("NOTA NO VALIDA")