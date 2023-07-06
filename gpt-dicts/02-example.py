#Crear un diccioanrio vacio
from optparse import Values


dic = {}

dic = {"name": "nayaret", "age": 23, "city": "Santiago"}

print(dic["name"])
print(dic["age"])
print(dic["city"])

#modificar un valor existente
dic["age"] = 30
print("----------------")
print(dic["age"])

#agregar un nuevo par llave-valor
dic["hero"] = "Batman"
print("--------------")
print(dic)

#Eliminar un par llave-valor
del dic["age"]
print("--------------")
print(dic)

#Revisar si existe una llave en el diccionario
if "hero" in dic:
    print(f"El héroe de acción es {dic['hero']}")

#obtener el listado de llaves 
keys = dic.keys()#metodo para sacar llaves y valores
values = dic.values()

print(keys)
print(values)

#el metodo items nos entrega una lista con los pares llave-valor que podemos despues recorrer
items = dic.items()
print(items)

#recore el arreglo con for e items
for key, value in dic.items():
    print(key, ':', value)
print("-------------------------")

#Otra forma de recorrer el diccionario:
for key in dic.keys():
    print(key, ':', dic[key])


