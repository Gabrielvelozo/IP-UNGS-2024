"""
a) Sabiendo que la pantalla de la consola tiene 80 caracteres de ancho, hacer un programa que, dada una palabra,
la escriba en el centro de la pantalla

"""
us=input("Ingrese una palabra. ")
cantidad_palabra= len(us)

imprimir=(160-cantidad_palabra)//2
centrar=" " * imprimir + us
print(centrar)

