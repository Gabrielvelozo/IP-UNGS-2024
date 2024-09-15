"""
1/0! + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6!
b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
da la calculadora?

"""
import math

e=1
factorial=1
i=1
while math.e-e >0.01:
    factorial *=i
    e += 1/factorial
    print(math.e - e) # Validar si esta bien el buble en cada iteracion.
    i+=1
print(f"A partir del término {i-1}, el valor es menor a 0.01 : {math.e - e}")

