"""
c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
256. Es decir, 1**1 2**2 3**3 4**4
"""
n=int(input("Ingrese un número n > 0: "))
acumulador=1
for i in range(1,n+1):
    print(f"{acumulador**i}",end=" ")
    acumulador+=1
