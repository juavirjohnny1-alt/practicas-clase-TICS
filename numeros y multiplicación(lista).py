#LISTA:NÚMEROS Y MULTIPLICACIÓN
print("LISTA DE NÚMEROS Y MULTIPLICACIÓN")
numeros=[]
resultados=[]
i=0
#Solicitar numeros
while i<5:
    num=int(input("Ingresa un número: "))
    numeros.append(num)
    i=i+1
#Solicitar por cuantas veces se desea multiplicar el numero
multiplicador=int(input("¿Por cuánto deseas multiplicar?: "))
#Multiplicación y lista de resultados
for num in numeros:
    resultado=num * multiplicador
    resultados.append(resultado)
#Lista de números originales
print("Números originales: ",numeros)
#Lista de resultados de las multiplicaciones
print("Resultados: ",resultados)
#Buscar un número en los resultados
buscar=int(input("¿Qué número deseas buscar?: "))
if buscar in resultados:
    print("El número si aparece en los resultados")
else:
    print("El número no aparece en los resultados")