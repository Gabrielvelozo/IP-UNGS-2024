"""
Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
b el intermedio y en c el mayor (es decir, ordenará los valores).
"""
x=int(input("ingrese un valor a x:"))
y=int(input("ingrese un valor a y:"))
z=int(input("ingrese un valor a z:"))
a=0
b=0
c=0

if x<=y and x<=z:
    a=x
    if y<=z:
        b=y
        c=z
    else:
        b=z
        c=y
elif y<=x and y<=z:
    a=y
    if x<=z:
        b=x
        c=z
    else:
        b=z
        c=x
else: 
    a=z
    if x<=y:
        b=x
        c=y
    else:
        b=y
        c=x

# Mostrar los resultados
print("El menor valor es:", a)
print("El valor intermedio es:", b)
print("El mayor valor es:", c)