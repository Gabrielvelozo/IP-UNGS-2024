"""
c) Hacer un programa que permita al usuario elegir un número n y un número c, y
luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
"""
n=int(input("Ingrese un número n: "))
c=int(input("Ingrese un número c: "))

for num in range(1,c+1):
    print(f"{n+num}",end=" ")

print("\n")

contador=1
while contador<=c:
    print(f"{n++ contador}",end=" ")
    contador+=1
