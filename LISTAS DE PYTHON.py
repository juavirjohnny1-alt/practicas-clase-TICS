#LISTAS DE PYTHON
#Almacenar datos
print("Lista de datos:")
deportes=["futbol","basquet","voleyball"]
print(deportes)
#Mostrar un elemento de la lista
print("Mostar el elemento número 1 de la lista:")
print(deportes[1])
#Agregar cosas u elementos a la lista
print("se agregara a la lista beisbol:")
print("Nueva lista:")
deportes.append("beisbol")
print(deportes)
#Agregar elementos en una posicion dada
print("Se agregara atletismo a la posicion 1:")
print("Nueva lista:")
deportes.insert(1,"atletismo")
print(deportes)
#Modificar elemento en una posición
print("Se cambiara a box en la posición 2:")
print("Nueva lista:")
deportes[2]="box"
print(deportes)
#Eliminar elenmtos de la lista
print("Se quitara atletismo de la lista")
print("Nueva lista:")
deportes.remove("atletismo")
print(deportes)
#Mostra la lista (cada elemento)usando for
print("Se mostrara cada deporte de la lista por separado:")
for deporte in deportes:
    print(deporte)