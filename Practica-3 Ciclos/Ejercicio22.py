"""
Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
suerte debe ser elegido al azar)

"""
import random
bandera=True
while bandera:
    numero=int(input("Ingrese un número apostar: "))
    monto=int(input("Ingrese un monto a jugar: "))

    quinela=random.randrange(0,100)

    if numero==quinela:
        print(f"Ganaste! Número gandor: {quinela}, elegiste el: {numero}. PREMIO: $ {monto*70}")
        bandera=False
    else:
        print(f"No ganaste, salio: {quinela}")
    


