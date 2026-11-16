#LISTA:NUMEROS PARES
print("LISTA DE NUMEROS PARES")
numeros=[]
numPares=[]
i=0
#Solicitar números
while i<10:
    num=int(input("Ingresa un número: "))
    numeros.append(num)
    i=i+1
print("Números pares: ")
#Lista de numeros pares ingresados mostrados por separado
for num in numeros:
    if num % 2==0:
        print(num)
        numPares.append(num)
#Lista de números pares ingresados mostrados en lista 
print("Lista de números pares: ")
print(numPares)