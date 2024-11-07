#a) Hacer una función que reciba dos enteros y retorne el mayor

def mayor(n1,n2):
    if n1>n2: return n1
    else: return n2

#print(mayor(7,3))

#b) Hacer una función que reciba tres enteros y retorne el mayor.

def mayorDeTres(n1,n2,n3):
    if n1>n2 and n1>n3:
         return n1
    if n2>n1 and n2>n3:
        return n2
    else: return n3

print(mayorDeTres(40,12,120))