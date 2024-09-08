"""
Se tiene la siguiente lista con DNIs de personas.
30612453
23763290
21448503
34582048
15364857
Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.
"""

b=36614414
g=34227796
n=58067465
o=52739937

dni=int(input("Ingrese un nuevo DNI: "))

if dni==b or dni==g or dni==n or dni==o: print("El DNI existe en el listado")
else: print("Se ingreso un nuevo DNI.")