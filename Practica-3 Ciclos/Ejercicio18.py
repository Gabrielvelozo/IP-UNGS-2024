"""
1/0! + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6!
a) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
da la calculadora?

"""
n=int(input("Ingrese un numero n : "))
e=1
factorial=1
for i in range(1,n+1):
    factorial *=i
    e += 1/factorial
print(f"El numero aproximado de e para los {n} terminos es : {e}")

