#Defiir una función mostrarEnUnaLinea q tome una lista de enteros y muestre todos sus elementos en una linea separados por espacios.

def mostrarEnUnaLinea(lista):
   
    for elem in lista:
        print(elem, end=" ")
    


lista=[1,2,6,6,5,77,8,90]
mostrarEnUnaLinea(lista)
      