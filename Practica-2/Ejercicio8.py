"""
Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
comienzo y al fin del período
"""

kw200= 480
kwEx= 25.5
impuestos=78
valorC=int(input("Ingrese el consumo inicial medidor: "))
valorF=int(input("Ingrese el consumo final del medidor: "))

consumoMensual=valorF-valorC
tarifaExedente=(consumoMensual-200)*kwEx
tarifaFinal=tarifaExedente+kw200+impuestos
print(f"El importe que se debe facturar por los consumos detallados es de: $ {tarifaFinal}")