"""
Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos
vocales unidas).

"""
cadena=input("Ingrese una palabra: ")

vocales=0
for char in cadena:
    if char == "a" or "e" or "i" or "o" or "u":
        vocales+=1
    else: vocales=0
    

if vocales >=2: print(f"{cadena}, es diptongo")
else: print(f"{cadena}, no es diptongo")


