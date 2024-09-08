"""
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
"""
n = int(input("Ingresa un número entero: "))

for num in range(1,6):
    print(f"{n+num}",end=" ")


print("\n")


# Inicializar un contador para determinar cuántos números se han mostrado.
contador = 0

# Usar un ciclo while para mostrar los siguientes 5 números
while contador < 5:
    # Mostrar el siguiente número natural
    print(n + 1 + contador, end=" ") # n SIEMPRE ES n.
    
    """
    Cuando contador es 0, n + 1 + contador es 11.
    Cuando contador es 1, n + 1 + contador es 12.
    Cuando contador es 2, n + 1 + contador es 13, y así sucesivamente.
    """
    # Incrementar el contador
    contador += 1