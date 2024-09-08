"""
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el
3 (8, 7, 6, 5, 4, 3).
"""
i=8 
while i>=3:
    print(f"{i}",end=" ")
    i-=1

print("\n")   

for num in range(8,2,-1):
    print(num,end=" ")
