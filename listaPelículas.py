#LISTAS DE PELÍCULAS
#Programa que agrega películas a una lista
#Ponerle nombre a mi lista
peliculas=[]
#Preguntar cuntas películas desea agregar
print("Lista de películas")
cantidadPeliculas=int(input("¿Cuántas películas deseas agregar: "))
#Valor inicial para el while
i=0
#Mientras i sea menor a catidad ejecutar
while i<cantidadPeliculas:
    #Pregunatar películas
    peli=input("Ingresa la película: ")
    #Agregar película a la lista
    peliculas.append(peli)
    #Muestra la lista
    print(peliculas)
    i=i+1
#Buscar una película en la lista
#Preguntar la película a buscar
peliBuscar=input("¿Qué película buscas?: ")
if peliBuscar in peliculas:
    print("Si esta")
else:
    print("No esta pero dejame la agrego")
    peliculas.append(peliBuscar)
    print(peliculas)
#LO EXTRA...
#Solicitar una película para borrar
peliculaBorrar=input("¿Qué película deseas borrar?: ")
#Borrar la película
peliculas.remove(peliculaBorrar)
#Mostra la lista
print(peliculas)