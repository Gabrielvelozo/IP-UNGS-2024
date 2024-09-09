"""
f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
muestre en pantalla los últimos c divisores de n
"""
# Solicitar al usuario que ingrese dos números positivos
c = int(input("Ingresa el valor de c (número de divisores a mostrar): "))
n = int(input("Ingresa el valor de n (número del cual encontrar los divisores): "))

# Verificar si los números ingresados son positivos
if c <= 0 or n <= 0:
    print("Ambos números deben ser positivos.")
else:
    # Contar el total de divisores y prepararse para almacenar los últimos c divisores
    contador_divisores = 0
    divisor_actual = 0
    divisores_mostrados = 0

    # Primero contamos el total de divisores
    for i in range(1, n + 1):
        if n % i == 0:
            contador_divisores += 1

    # Verificar si hay suficientes divisores
    if contador_divisores < c:
        print(f"No hay suficientes divisores para mostrar. Solo hay {contador_divisores} divisores.")
    else:
        # Mostrar los últimos c divisores
        # Recorremos nuevamente para encontrar y mostrar los últimos c divisores
        for i in range(1, n + 1):
            if n % i == 0:
                divisor_actual = i
                if contador_divisores > c:
                    contador_divisores -= 1
                else:
                    print(divisor_actual,end=" ")