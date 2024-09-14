"""
El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
1 - 1/2 + 1/3 - 1/4 + 1/5
c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
da la calculadora?
"""
import math
suma=0
i=1
while abs(math.log(2) - suma) >0.01:
    suma+= (-1)**(i+1)/i
    i+=1
print(f"A partir del termino {i-1}, el valor es menor a 0.01 : {suma-math.log(2)}")