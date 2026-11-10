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
#Lsiata de resultyados de las multiplicaciones
print("Resultados: ",resultados)