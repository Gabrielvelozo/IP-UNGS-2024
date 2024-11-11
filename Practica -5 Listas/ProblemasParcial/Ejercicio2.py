"""Hacer un programa para automatizar la inscripción de estudiantes a materias de la Universidad. Usted dispone de una 
lista con los DNI de los estudiantes y otra con las materias a las que desean inscribirse. El programa debe modificar es
tas listas de forma tal que solo queden DNI y materias aceptadas.
Para ello cuenta con las siguientes funciones: 
 correlativas(materia): Devuelve una lista de las correlativas a esa materia. 
 aprobada(dni, materia): Devuelve verdadero si el estudiante tiene aprobada la materia. 
 horario(materia): Devuelve el horario de la materia. 
 controlaSuperposicion(dni, horario) Devuelve verdadero si el estudiante tiene libre ese horario. 
"""

listaDni=[30435473,35552144,11421159,28667796,26959663,30435473,29927766]
materiasEstudiantes=["InglesI","Programación","Ingles","Matemática","Programación","Ingles"]


for i in range(len(listaDni)):
    dni=listaDni[i]
    materia=materiasEstudiantes[i]

correlativasMateria=correlativas(materia)
cumpleCorrelativas=True 
for corr in correlativasMateria:
    if not aprobada(dni,corr):
        cumpleCorrelativas=False
        

