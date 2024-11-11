#se debe controlar que los automóviles no superen 100 km/h y en caso de hacerlo se les enviará una multa a sus hogares, si es reincidente
#la multa se duplica
#darPatentes(ruta),Dada una ruta nacional devuelve una lista con todas las patentes de los autos que pasaron en el día.
#controlVelocidad(patente),Recibe un número de patente y devuelve la velocidad a la q cruzó el radar dicho automóvil.
#reincidente(patente),Devuelve True en caso de que la patente ya tenga multas por exceso de velocidad.
#costoActual(),No recibe parámetros y devuelve el costo por superar la velocidad permitida.
#enviarMulta(patente, costo),Manda una multa al domicilio del propietario del automóvil con el costo

ruta=8

def control(ruta):
    listaPatentes=darPatentes(ruta)
    cobrar=costoActual()
    for patente in listaPatentes:
        if controlVelocidad(patente)>100:
            cobrar
        if reincidente(patente):
            cobrar*2
                
    return enviarMulta(patente,cobrar)


    
           

