"""
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta
el 6 pero salteando de a tres (15, 12, 9, 6).
"""
i=15
while i>=6:
    print(f"{i}",end=" ")
    i-=3
    
print("\n")

for num in range(15,5,-3):
    print(num, end=" ")