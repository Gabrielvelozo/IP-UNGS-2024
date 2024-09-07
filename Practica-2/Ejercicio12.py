"""
Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
valores de las variables y mostrarlos de mayor a menor.
"""

a=int(input("Ingrese un valor para a: "))
b=int(input("Ingrese un valor para b: "))

if a<b: 
  aux=a
  a=b
  b=aux
  print(f"a: {a} - b: {b} INTERCAMBIO")
elif a>b: print(f"a: {a} - b: {b} ")
else: print("SON IGUALES")