#Con lsitas o diccionarios podemos representar estructuras completas similares a lo que encontramos en el mundo real. Por ejemplo, pordriamos tener un listado de estudiantes.
#Cada estudiante es un diccionario con nombre, apellido, curso y una lista de sus calificaciones
#Ej:

students = [
{
    "name": "Nayaret",
    "lastname": "Schaeffer",
    "course": "tejido 1",
    "grades": [100,90,95,100],
    "active": False
},
{
    "name": "Gabriel",
    "lastname": "Jimenez",
    "course": "Viajes espaciales",
    "grades": [90,100,85,100],
    "active": True
}
]

#Ejercicio manipular el arreglo de estudiantes para que muestre la siguiente información por cada uno
#Estudiante Nombre Apellido 
#Curso: Nombre del curso
#Promedio de notas: 0
#Estado: Activo/inactivo

for student in students:
    print("__________________________________________________")
    print("estudiante:", student["name"], student["lastname"])
    print("curso:", student["course"])

    sum = 0
    grades = student["grades"]
    for grade in grades:
        sum +=1
    
    print("Promedio de notas", sum/len(grades))

    if student["active"]:
        print("Estado: Activo")
    else:
        print("Estado inactivo")


