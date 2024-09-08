"""
Realizar un programa que solicite dos números y realice la división entre ellos, no se debe permitir que el denominador sea 0.
"""

#Inicia la condición
denominador=0

#Aseguramos que al menos 1 vez va entrar al ciclo while.
while denominador==0:
    #Pedimos numerador y denominador.
    numerador=int(input("Ingrese el numerador: "))
    denominador=int(input("Ingrese el denominador: "))
    #Valida si denominador es igual a 0.
    if denominador ==0:
        print("El denominador no puede ser 0.\nIngrese otro número.")
    #sale del ciclo

resultado= numerador/denominador
#imprimimos
print(f"El resultado es {resultado}")
    

