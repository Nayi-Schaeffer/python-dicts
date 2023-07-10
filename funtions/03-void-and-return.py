# En unas de las opciones que hemos visto entregan de vuelta su resultado 
#Ej: input() Entrega lo escrito por el usuario y luego lo podemos asignar a una variable
from unicodedata import name
from unittest import result


name = input("Dime tu nombre:\n")

print(name)

test = print("Hola Mundo")

print(test)

#Las funciones que no retornar a nada o que retornan un valor especial **none** se les conoce como funciones void (vacío)

#Si queremos que nuestra función retorne un valor, lo indicamos con la palabra **return**
print("-----------------------")
def multiply_by_two(number):
    return number * 2

result = multiply_by_two(2)
print(result)
