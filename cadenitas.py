print("Nombre y frase en mayuscula y minusculas:")
nombre="Jonathan"
frase="Mi color favorito es el azul"
print(nombre)
print(frase)
#Mostrar el nombre y la frase en mayusculas
print("En mayusculas:")
print(nombre.upper())
print(frase.upper())
#Moatrar el nombre y la frase en minuscula
print("En minusculas:")
print(nombre.lower())
print(frase.lower())
#Obtener un carácter en una posición
print("Posicion de una letra de mi nombre [5]:")
letra1=nombre[5]
print(letra1)
print("Posicion de una letra de la frase[4]:")
letra2=frase[4]
print(letra2)
#Separar frase y nombre
print("Separacion de la frase:")
frase2="Mi-comida-favorita-es-la-pizza"
print(frase2.split("-"))
print("Separación de el nombre completo:")
nombreCompleto="Jonathan Juárez Viramontes"
print(nombreCompleto.split(" "))
#Dos primeras letras del nombre
print("Letras determinadas que solicite de mi nombre completo 0:2:")
letras1=nombreCompleto[0:2]
print(letras1)
#Cambio de frase 
print("Cambio de una palabra en la frase original, el azul por el verde:")
nuevaFrase=frase.replace("azul","verde")
print(nuevaFrase)
#Número de caracteres de la cadena: largo
print("Número de caracteres de la frase nueva:")
largoCadena=len(nuevaFrase)
print(largoCadena)