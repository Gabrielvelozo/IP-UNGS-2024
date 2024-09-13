"""
d)
Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla las n primeras sumas parciales de la sucesión an = 1/n**2 

"""
n=int(input("Ingrese un número > 0: "))
suma=0
for i in range(1,n+1):
    suma+=1/(i**2) # Acumula valores.
    print(f"{suma}",end=" ")

# ¿A qué valor se va acercando la suma del inciso anterior a medida que utilizamos un valor alto de n?  pi**2/6
