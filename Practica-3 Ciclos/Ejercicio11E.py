"""
e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
muestre en pantalla los primeros c divisores de n
"""
c=int(input("Ingrese un número: "))
n=int(input("ingrese un número: "))

if c<0 and n<0:
    print("ingrese numeros postivos. Vuelva a intentar.")

else:
    contador=1
    for i in range(1,n+1):
        if n%i==0 and contador<=c:
            print(f"{i}",end=" ")
            contador+=1
