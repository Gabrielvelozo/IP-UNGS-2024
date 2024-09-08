"""
Realizar un programa que sume los primeros números impares hasta n. (n lo indica el usuario) 1+3+5+…+n=

"""
n=int(input("Ingrese un número: "))

i=1
suma=0
while i<=n:
    suma+=i
    i+=2
print(f"La suma de los primeros {n} números impares son {suma}")
