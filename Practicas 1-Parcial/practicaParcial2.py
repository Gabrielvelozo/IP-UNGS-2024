"""
 1 + 1/2 + 1/3 - 1/42 + 1/5 + 1/6  + 1/7 - 1/82+ 1/9  + 1/10 + 1/11 - 1/122 + 1/13
"""
suma=1
for i in range(2,14):
    if i==4:
        suma-=1/42
    elif i==8:
           suma-=1/82
    elif i==12:
            suma-=1/122
    else:suma+= 1/i
print(suma)

"""
2/3 + 3**2/4 + 4**3/5 + 5**4/6 + 6**5/7
"""
n=int(input("numero: "))
suma=0

for i in range(2,n+1):
    termino=i**(i-1)/(i+1)
    print(f"{i**(i-1)}/{(i+1)}")
    suma+=termino
print(suma)

