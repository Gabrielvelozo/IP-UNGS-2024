#Definir una función que tome un entero n y devuelva los primeros n primos.

def esPrimo(n):
    for i in range(1,n+1):
        if n%i==0:
            return True
    return False

def primerosPrimos(x):
    primos=[]
    numero=2
    while len(primos)<x:
        if esPrimo(numero):
            primos.append(numero)
        numero+=1

    return primerosPrimos

num=10
print(primerosPrimos(num))