"""
b) 
Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla los n primeros términos de la sucesión  an = 2n - 1

"""
n=int(input("Ingrese un número > 0: "))

for i in range(1,n+1):
    print(f"Los terminos de la sucesión an=2n-1 (n={i}) = {2*i-1}")
