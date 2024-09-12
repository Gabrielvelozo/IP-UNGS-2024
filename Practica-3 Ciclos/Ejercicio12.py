"""
Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n.

"""


n=int(input("Ingrese un número n: "))



if n<0:
    print("Debe ingresar un número positivo: ")
    
else:
    for x in range(1,n+1):
        print(f"El producto de los números: {x} X {n}= {x*n}")        

