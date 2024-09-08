"""
Realizar un programa que sume los primeros n números impares. (n lo indica el usuario) 

"""
n=int(input("Ingrese un número: "))

i=1 # CONTADOR DE IMPARES.
suma=0 # ACUMULADOR.
contador=0 # VALIDAR VUELTAS DEL CICLO IGUAL A LAS INGRESADAS POR n.
while contador<n:
    suma+=i
    i+=2
    contador+=1
print(f"La suma de los primeros {n} números impares es {suma}")

