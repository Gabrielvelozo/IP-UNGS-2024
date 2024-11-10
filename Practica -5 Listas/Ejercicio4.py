#Definir función llamada laMasCorta q tome 2 listas devuelva la q tenga menos elementos. Si tienen igual cantidad, deberá devolver la primera

def laMasCorta(lista1,lista2):
    if len(lista1)<=len(lista2):
        return lista1
    else:
        return lista2
    
lisUno=[1,2,3]
lisDos=[0,2,5]
print(laMasCorta(lisUno,lisDos))