"""
Hacer un programa que calcule la siguiente serie:
S= 10 + 2/3 - 4/5**3 + 6/7**5 - 8/9**7 + 10/11**9 -12/13**11
"""

suma=10

for i in range (1,7):
    #1Forma Calculando el termino con el indice i.
    termino= ((-1)**(i+1))*(2*i)/(2*i+1)**(2*i+1)
    print(f"(1)**(i+1): {(-1)**(i+1)} (2*i)/ : {(2*i)} (2*i+1): {(2*i+1)} (2*i+1): {(2*i+1)} Suma= {suma}")
    suma+=termino
print(f"suma - 1: {suma}")

signo=1
su=10
for i in range (1,7):
    #2Forma  con la variable signo 
   ter=((2*i)/(2*i+1)**(2*i+1))*signo
   signo=signo*(-1)
   su+=ter
print(f"suma - 2: {su}")

s=10
for i in range(1,7):
    #3Forma con condicionales.
    if i%2==0:
        s-=(2*i)/(2*i+1)**(2*i+1)
    else:
        s+=(2*i)/(2*i+1)**(2*i+1)
print(f"suma - 3: {s}")
