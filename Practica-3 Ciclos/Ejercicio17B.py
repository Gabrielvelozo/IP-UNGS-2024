"""
El número 1/4π se puede aproximar de la siguiente manera:
 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15
b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
da la calculadora?
"""
import math
suma=0
i=1
while abs((1/4)*math.pi-suma)>0.1:
    suma+= (-1)**(i+1)/(2*i-1)
    print(f"- {(1/4)*math.pi-suma}") # Validar lo resta.
    i+=1
    
print(f"A partir del término {i-1}, el valor es menor a 0.1 : {(1/4)*math.pi-suma}")