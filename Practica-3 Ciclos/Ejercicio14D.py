"""
d) 
Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla los n primeros términos de la sucesión  an = n**3 - n**2.

"""
n=int(input("Ingrese un número > 0: "))

for i in range(1,n+1):
    print(f"Los términos de la sucesión an=n**3-n**2 (n={i}) = {i**3-i**2}")
    