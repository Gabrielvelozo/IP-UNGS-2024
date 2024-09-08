"""
Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
costo por comunicación es de $12 y por cada segundo se cobra $1,5 hacer dicho programa. Se deben
ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
el precio a cobrar. Por ejemplo, si realizó 10 llamadas con un total de 4000 segundos el importe a pagar
sería de $6120
"""
qCall=int(input("Ingrese la cantidad de llamadas: "))
tCall=int(input("Ingrese el tiempo total de llamadas: "))
cobrar= qCall*12 + tCall*1.5
print(f"Importe a cobrar: ${cobrar}")