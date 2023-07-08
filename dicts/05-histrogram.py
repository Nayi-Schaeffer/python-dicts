# Un histograma de frecuencia sirve para representar cuantas veces aparece sierto elemento en una coleccion o mas en general sirve para resumir resultados.
#Supongamos que nos dan una palabra y necesitamos contar cuantas veces aparece cada letra en la palabra.

word = input("Dame una palabra:  ")


#Esta variable actua como acumuludador pero en forma de diccionario
letter_counter ={}

for letter in word:
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] =1

for letter in letter_counter:
    print(f"{letter}: {letter_counter[letter]}")