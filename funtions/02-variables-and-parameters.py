# Cuando creamos una variable dentro de una función, se dice que es una variable **local** que significa que sólo existe dentro de la función 
#Ej: 
#En este caso la variable full_name, solo existe dentro de la función. Tiene sus propias variables que no se filtran hacia afuera. En comptación eso se le llama ámbito o alcance. Es decir. La variable full_name es de ámbito local. 
def say_hello(name,lastname):
    full_name = f"{name} {lastname}"
    print(f"¡Hola {full_name}")

say_hello("Gabriel", "Jimenez")

#Esto es un error porque full_name sólo existe dentro del ámbito de la función say_hello
#print(full_name)



