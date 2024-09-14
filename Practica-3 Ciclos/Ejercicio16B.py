"""
El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
1 - 1/2 + 1/3 - 1/4 + 1/5
b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
da la calculadora? En python se puede aproximar este valor usando math.log(2)

"""
import math
suma=0
i=1

while abs(math.log(2) - suma) > 0.1: # ABS nos da el valor absoluto sin mirar el signo.
    suma+= (-1)**(i+1)/i
    i+=1
print(f"A partir del termino {i-1}, el valor es menor a 0.1: {suma-math.log(2)}")