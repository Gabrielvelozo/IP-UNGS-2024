"""
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
11 salteando de a 2 elementos (5, 7, 9 y 11)

"""
for num in range(5,12,2):
    print(num, end=" ")

print("\n")
i=5
while i<=11:
    print(f"{i}",end=" ")
    i+=2
    