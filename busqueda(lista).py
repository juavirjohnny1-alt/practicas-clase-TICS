#LISTA:BUSQUEDA
#Lista de nombres
print("Lista de busqueda de nombres")
nombres=["Ángel","Karla","Luis","Mateo","María","Luis","Karla"]
print(f"Los nombres que se tiene son: {nombres}")
#Nombre que se dea buscar en la lista 
nombreBuscar=input("¿Qué nombre deseas buscar?: ")
encontrado=False
contador=0
i=0
#Nombre en la posición
while i<len(nombres):
    if nombres[i]== nombreBuscar:
        encontrado=True
        contador=contador+1
        print("Encontado en la posición: ",i)
    i=i+1
#Nombre si encontrado
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece ",contador, "veces")
else:
#Nombre no encontrado
    print("Nombre no encontrado")