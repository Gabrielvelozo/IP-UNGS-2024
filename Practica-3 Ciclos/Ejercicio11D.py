"""
d) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla la suma de los divisores de n.

"""
n=int(input("ingrese un número n > 0: "))

if n<0: print("El numero debe ser positivo. Vuelva a ingreasar un número.")
 
else:
    contador=0
   
    for i in range(1,n+1):
         if n%i==0:
              
            contador+=i
print(f"La suma de los divisores de {n} es: {contador}",end=" ")