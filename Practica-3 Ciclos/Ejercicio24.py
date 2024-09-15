"""
¿Para qué números enteros distintos de cero es cierto que A + B + C = A x B x C ? (lo
curioso es que sólo hay una solución)

"""
# For anidado para tener combinanciones diferentes para A,B,C.
for a in range(-99,100):
    for b in range(-99,100):
        for c in range(-99,100):
            if a !=0 and b !=0 and c !=0: # Valida que NO sean A,B,C = 0.
                if a + b + c == a * b * c: # Si 
                    print(f"A= {a} - B= {b} - C= {c}")

