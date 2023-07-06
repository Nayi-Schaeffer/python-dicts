#si utilizamos un loop for para recorrer un diciionario, el for va a recorrer las llaves del diccionario y podemos utilizar las llaves para accceder a los valores 

some_dict = {
    "Name": "Nayaret",
    "Lastname": "Schaeffer",
    "weight": 62,
    "height": 1.59
    }

for key in some_dict:
    print(key, some_dict[key])