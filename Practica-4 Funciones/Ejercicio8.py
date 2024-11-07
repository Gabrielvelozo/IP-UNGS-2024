#a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad de divisores positivos de ese número.

def divisoresPositivos (numero):
    divisores=0
    for i in range(1,numero+1):
            if numero%i==0:
                divisores+=1

    return divisores

#print(divisoresPositivos(10))

#b) Escribir una función q tome un parámetro tipo entero y devuelva el valor True si se la llama con un número primo y False en caso contrario.

def validarPrimo (numero):
    contador=0
    for i in range (1,numero+1):
          if numero%i==0:
            contador+=1
    if contador<=2: return True
    else: return False

print(validarPrimo(100))