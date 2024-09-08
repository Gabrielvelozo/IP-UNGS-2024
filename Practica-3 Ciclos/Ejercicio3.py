"""
Modificar el programa anterior, para que pida al usuario un número entero e imprima la tabla de multiplicar de dicho número.

"""
# INICIADOR.
i=1
# SOLICITUD USER.
tabla=int(input("Ingrese el número de la tabla que desea saber: "))
# ITERACION MENOR/IGUAL A 10
while i<=10:
    #IMPRIME.
    print(f"{tabla} * {i} = {tabla*i}")
    # ACUMULADOR.
    i+=1

