"""
Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
a invertir y la cantidad de meses. Por ejemplo, si invierte 500 mil pesos por 4 meses el banco debería
devolverle 620 mil pesos.
"""
user=int(input("Ingrese el dinero a invertir: "))
meses= int(input("Ingrese los meses del plazo: "))
devolver= (user*0.06) * meses + user
print(f"{devolver}")