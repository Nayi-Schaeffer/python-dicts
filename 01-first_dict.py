#Diciionario es como una lista pero mas general, es decir, es un diccionario los incides pueden ser casi de cualquier tipo.
#En los diccionarios indices son llamados *Llaves* o "keys" y tiene asociado sus respectivos valores

#Ej:
from ctypes.wintypes import HLOCAL


English_to_spanish = {}#Crea un diccionario vacio
English_to_spanish = {"one":"uno","two":"dos"}

#Los elementos se agregan en pares, es decir llave-valor.

English_to_spanish["hello"] = "hola"
English_to_spanish["bye"] = "Adios"

print(English_to_spanish)

#Para acceder al volor de las llave en espicifico usamos la anotación con []
print(English_to_spanish["one"])

#El valor de un diciionario se puede obtener con la función len() , igual que con las listas
print(len(English_to_spanish))# >=4






