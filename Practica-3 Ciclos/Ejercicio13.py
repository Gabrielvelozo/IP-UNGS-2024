"""
Hacer un programa que reciba un número m y determine el primer n para el cual la suma
1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

"""
m=int(input("Ingrese un número m: "))

# Acumula el valor de los números.
suma=0

# Contar los números que van en el ciclo.
n=0
# ciclo FOR
for i in range(1,m+1):
    n = i
    suma+=i
    if suma>m:
        break


# Ciclo While.
"""while suma<=m:
    # Incrementamos n en cada iteración.
    n+=1
    # Acumula el valor de n.
    suma+=n"""
    
print(f"RETORNAR: {n}")

