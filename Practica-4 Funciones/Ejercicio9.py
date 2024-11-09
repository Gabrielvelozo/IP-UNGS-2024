#a) Hacer una función que reciba dos enteros y retorne el mayor

def mayor(n1,n2):
    if n1>n2: return n1
    else: return n2

a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
c=int(input("ingrese un numero: "))
#b) Hacer una función que reciba tres enteros y retorne el mayor.

masGrande=mayor(mayor(a,b),c)
print(masGrande)



