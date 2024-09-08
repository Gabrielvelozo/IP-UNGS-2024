"""
Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres
variables, x, y, y z. El programa deberá intercambiar circularmente los valores de x, y y z, es decir, x
debe tomar el valor de y, y el de z y z el de x. Y luego mostrarlos en pantalla:
El valor de x es: <x>
El valor de y es: <y>
El valor de z es: <z>
donde en lugar de <x>, <y> y <z> deberá mostrarse el valor de las respectivas variables.
"""
x=int(input("Ingrese el valor de X: "))
y=int(input("Ingrese el valor de Y: "))
z=int(input("Ingrese el valor de Z: "))

#Rotar los valores X,Y,Z con la ayuda del aux.
aux=x
x=y
y=z
z=aux
print(f"X: {x}\nY: {y}\nZ: {z}")