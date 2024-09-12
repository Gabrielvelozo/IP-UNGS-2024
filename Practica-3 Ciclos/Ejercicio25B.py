"""
Escribir un programa que pida al usuario un número n y muestre n líneas de
1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
mostrar:
*
**
***
****
*****

"""
n=int(input("ingrese un número para n: "))
asterisco=0
for i in range(1,n+1):
    asterisco=i*"*"
    print(asterisco)