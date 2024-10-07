"""
El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
1 - 1/2 + 1/3 - 1/4 + 1/5

a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
que muestre la aproximación de ln(2) con esa cantidad de términos.

"""

"""terminos=int(input("Ingrese la cantidad de terminos a sumar: "))
suma=0
for i in range(1,terminos+1):
    termino= (-1)**(i+1)/i # (-1)**(n+1) / n
    suma+=termino
    print(f"Termino: {termino} | Suma: {suma}")"""

S = 10  # Iniciamos con el primer término que es 10

for i in range(1, 7):
    # Calcular directamente el término basado en i
    termino = ((-1) ** (i + 1)) * ((2 * i) / ((2 * i + 1) ** (2 * i + 1)))

    # Sumar o restar el término a S
    S += termino
    print("El valor de S es:", S)

# Imprimir el valor final de S
"""print("El valor de S es:", S)"""