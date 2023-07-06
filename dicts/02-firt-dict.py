English_to_spanish = {"one":"uno","two":"dos"}#Crea un diccionario con dos elementos

#Podemos decir si cierta llave esta presente en el diccionario con la palabra reservada in

if "one" in English_to_spanish:
    print("Si esta la llave one")
    print("Su valor es:", English_to_spanish["one"])

#Si tratamos de acceder a una llave que no existe, cometeremos un error de llave 

#print(enlish_to_spanish["three"])

