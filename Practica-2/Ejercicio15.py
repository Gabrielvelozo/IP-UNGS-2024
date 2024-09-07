"""
Escribe un programa que pida los coeficientes de una ecuación de primer grado (ax + b = 0)
y escriba la solución. Recuerda que una ecuación de primer grado puede no tener solución, tener
una solución única, o que todos los números reales sean solución.
"""
a=float(input("Ingrese el coeficiente de x: "))
b=float(input("Ingrese el coeficiente de b: "))
if a==0 and b==0: print("La ecuacion tiene infinitas soluciones")
elif a==0 and b!=0: print("La ecuacion no tiene soluciones")
else:
  x=(-b/a)
  print(f"La solucion es: {x}")