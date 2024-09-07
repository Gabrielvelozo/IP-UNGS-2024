"""
Un año es bisiesto si es múltiplo de 4. Pero no siempre, las excepciones son los años múltiplos
de 100 que no son múltiplos de 400 (1900 no es bisiesto pero 2000, sí). Escribir en papel un
programa que diga si un año ingresado por el usuario es bisiesto, realizar varias pruebas de
escritorio, luego pasarlo a Python y verificar los resutlados.
"""
year=int(input("Ingrese un año para validar si es bisiesto: "))
if (year%4==0 and year%100!=0) or (year%400==0): print(f"AÑO:{year} BISIESTO")
else: print("NO ES BISIESTO")