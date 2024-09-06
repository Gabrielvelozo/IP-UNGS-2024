"""
Determinar cuántos segundos tiene una hora, y cuántos tiene un día.
Escribir una expresión matemática que transforme un lapso de tiempo expresado en segundos a uno
expresado en minutos.
Escribir otra para transformar a horas y una última que transforme a días.
Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos
minutos son, así como también cuantas horas y cuantos días.
"""

user=int(input("Ingrese la cantidad de segundos a transformar: "))
print(f"Dias: {user//86400}\nHoras: {user//3600}\nMinutos: {user//60}")