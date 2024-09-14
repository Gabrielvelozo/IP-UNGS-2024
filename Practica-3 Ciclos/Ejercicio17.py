"""
El número 1/4π se puede aproximar de la siguiente manera:
        1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15
a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
que muestre la aproximación de π con esa cantidad de términos.
""" 
terminos=int(input("Ingrese la cantidad de términos a calcular: "))
suma=0
for i in range(1,terminos+1):
    # Agrego la variable (termino) para ver como itera los signos + , -
    termino= (-1)**(i+1)/(2*i-1) # LA FORMULA ES (-1)**n+1 / 2n-1
    suma+=termino
    print(f"Termino: {termino} | Suma: {suma}")

  