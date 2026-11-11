#LISTA:NOMBRE DE PERSONAS
print("LISTA DE NOMBRE DE PERSONAS")
nombres=[]
i=0
#Solicitar los nombres de las personas
while i<5:
    nombre=input("Ingresa un nombre: ")
    nombre=nombre.upper()
    nombres.append(nombre)
    i=i+1
#Mostra los nombres de la lista por separado
print("Lista de los nombres de personas ingresados:")
for nombre in nombres:
    print(nombre)