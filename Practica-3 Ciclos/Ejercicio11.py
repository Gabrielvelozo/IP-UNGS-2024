"""
a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla todos los divisores de n.
"""
n=int(input("ingrese un número n > 0: "))

if n<0:
    print("Debe ingresar un número mayor a 0. Vuelva a intentar.")
else:
    for i in range(1,n+1):
        if n%i==0:
            print(f"{i}",end=" ")
        
      
        

