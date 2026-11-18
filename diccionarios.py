#Listas
alumnos=["Juanito","Angelito"]
#Diccionarios
print("Diccionarios de los alumnos ")
alumno1={
    "nombre":"Juanito",
    "edad":15,
    "promedio":8.2
}
alimno2={
    "nombre":"Angelito",
    "edad":18,
    "promedio":10
}
#Consultar valores
#Forma 1
print("Nombre:", alumno1["nombre"])
#Forma 2
print("Nombre:",alumno1.get("nombre"))
#Modificar/Editar algun campo
alumno1["nombre"]="Pedrito"
print("Nombre:",alumno1.get("nombre"))
#Mostar CLAVE:VALOR todos los campos
for clave, valor in alumno1.items():
    print(clave, ":", valor)