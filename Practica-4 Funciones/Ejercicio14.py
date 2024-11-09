"""
 Hacer un programa que solicite al usuario un número entero positivo e indique cuál es el
 número primo mayor más cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
 programa devolverá 29 (29 es el número primo más cercano mayor que 24). Si el usuario ingresa
 5 el programa devolverá 7.
"""
def primoMasCercano (x):
    primoMayor=0
    for i in range(x,(x*2)):
        if 