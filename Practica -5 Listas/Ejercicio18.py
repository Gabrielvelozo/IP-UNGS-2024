#Definir una función que tome un entero n y devuelva los primeros n primos.

def numerosPrimos(num):
    lista=[]
    for i in range(1,num+1):
        if num%i==0:
            lista.append(i)
    return lista

def primosPrimosDeN(num):
    primos=[]
    contador=1
    while len(primos)<num:
        if numerosPrimos(contador):
            primos.append(contador)
            contador+=1
    return primos

print(numerosPrimos(5))
