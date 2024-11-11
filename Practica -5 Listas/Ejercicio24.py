#cobertura(cliente): retorna un string con los valores "Oro" o "Plata", correspondiente al tipo de cobertura del cliente.
#usados(cliente): retorna un entero que representa la cantidad de servicios que ya utilizó el cliente.
#radioDeCobertura(cliente, localidad): devuelve True si el cliente se encuentra dentro del radio de cobertura cubierto por la empresa.

def pagara(cliente,localidad):
    costo=0
    if cobertura(cliente)=="plata" and usados()>5:
        costo+=50
    if radioDeCobertura(cliente,localidad)==False:
        costo+=30
    return costo


 

