#Programa para calcular áreas 
#Area cuadrado
print("Área del cuadrado")
lado=float(input("Ingresa la medida de un lado:"))
areaCuadrado=lado*lado
print("El Área del cuadrado es:",areaCuadrado)
#Área de un triangulo
print("Área del triangulo")
base=float(input("Ingresa la medida de la base:"))
altura=float(input("Ingresa la medida de la altura:"))
areaTriangulo=base * altura / 2
print("El Área del triangulo es:",areaTriangulo)
#Área de un trapecio
print("Área del trapecio")
baseMayor=float(input("Ingresa la medida de la base mayor:"))
baseMenor=float(input("Ingresa la medida de la base menor:"))
altura=float(input("Ingresa la medida de la altura:"))
areaTrapecio=(baseMayor + baseMenor) * altura / 2
print("El Área del trapecio es:",areaTrapecio)
#Área de un círculo
print("Área del círculo")
radio=float(input("Ingresa la medida del radio:"))
areaCirculo=3.1416 * (radio * radio)
print("El Área del círculo es:",areaCirculo)
#Área de un pentagono
print("Área del pentagono")
perimetro=float(input("Ingresa la medida del perimetro:"))
apotema=float(input("Ingresa la medida de la apotema:"))
areaPentagono=(perimetro * apotema) / 2
print("El Área del pentagonoes:",areaPentagono)