
#d) ¿Qué imprime el siguiente programa?
cadena = ""
for letra in "se viene el frio":
	if letra != "e":
		cadena = letra + cadena
	else:
		cadena = cadena + letra
	
print(cadena)
