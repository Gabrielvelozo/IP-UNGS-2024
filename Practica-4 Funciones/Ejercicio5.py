# Definir una función que devuelva el valor absoluto de un número. (Hacerlo sin utilizar la función abs)

def absoluto(numero):
    if numero>0: return numero
    else: return (numero)*-1

print(absoluto(-5))