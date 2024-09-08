"""
Realizar un programa que sume los primeros n números naturales. (n lo indica el usuario) 1+2+3+4+…+n = 

"""

n=int(input("Ingresar un número: "))

i=1
suma=0
while i<=n:
    suma+=i
    i+=1
print(f"La suma de los primeros {n} números naturales es {suma}")