#Ejercicio 1: (2.5 puntos, 0.5 cada ítem)

#a) Si la variable n es un entero y la guarda del if es,  n!= -5 or n > 0 ¿Cuánto debe valer n para que no se cumpla la guarda?
n= -7
if n!= -5 or n>0:
	print("hola")
else: print("chau")
# n debe valer -5. Mi respuesta fue, 0. No la pense.

#b) Si la variable i vale -2 y la guarda de un condicional es  i<= -2 and i>= -2 ¿Se ejecuta la rama afirmativa o negativa del condicional?
i=-2
if i<=-2: print("afirmativo")
else: print("negativa")
# Afirmativa. Respuesta, OK.

#c) ¿Para qué valores de la variable entera m la siguiente condición es verdadera?:  m <= 3 or m > 2
m= 2
if m<=3 or m >2: print("Me salio bien!")
else: print("Muy mal!!")
# m=2. Respondi mal OTRA VEZ. Para todos los numeros enteros

#d) ¿Qué imprime el siguiente programa?
cadena = ""
for letra in "se viene el frio":
	if letra != "e":
		cadena = letra + cadena
	else:
		cadena = cadena + letra
	
print(cadena) # oirf l niv seeee. Al realizar la prueba en papel lo entendi.

#e) ¿Cuántas iteraciones realiza el siguiente ciclo?
cont= 11
while (cont> 6):
	print ("Hoy tenemos recuperatorio del Primer Parcial  de IP")
	cont = cont - 1
	
# 5 Iteraciones.
