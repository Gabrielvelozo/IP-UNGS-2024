#a) Escribir una función que reciba dos números reales como parámetros y retorne su promedio.
#b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla el resultado de llamar a la función del primer inciso.

def promedio (n1,n2):
    return (n1+n2)/2    

uno=int(input("Ingrese un numero: "))
dos=int(input("Ingrese un numero: "))
print(promedio(uno,dos))


#c) Idem de los dos anteriores pero con tres números. Escribir la función en el mismo archivo donde se escribió la del item a.

def promedio (n1,n2,n3):
    return (n1+n2+n3)/2 