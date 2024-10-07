
n=int(input("numero: "))
suma=0
divisores=0
for i in range(1,n+1):
    if n%i==0:
        divisores+=1
        suma+=i
    
print(f"Los divisores de {n}, son: {divisores} y la suma de ellos es: {suma}")