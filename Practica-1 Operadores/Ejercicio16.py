"""
La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada
denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda:
El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.
"""
cajero=int(input("Ingrese la cantidad de dinero a retirar: "))

p10000= cajero//10000
cajero= cajero%10000    
p5000= cajero//5000
cajero= cajero%5000
p2000= cajero//2000
cajero= cajero%2000
p1000= cajero//1000
cajero= cajero%1000
p500= cajero//500
cajero= cajero%500
print(f"10K: {p10000}\n5K: {p5000}\n2K: {p2000}\n1K: {p1000}\n500: {p500}")
