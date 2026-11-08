#CADENAS DE PYTHON
#Solicitar una cadena o string
palabra=input("Escribe algo:")
#Comprobar si una palabra contiene una letra
letra=input("Escribe una letra:")
if letra in palabra:
    print("La letra si esta en la palabra")
else:
    print("La letra no esta")
#Comprobar cuántas veces aparece una letra
cantidad=palabra.lower().count(letra)
print("la letra aparece",cantidad,"veces")
#Remplazar una letra
palabraNueva=palabra.replace(letra,"x")
print(palabraNueva)
#Contar cantidad de caracteres en la palabra
cantidadLetras=len(palabra)
#Verificar si una palabra tiene más de 5 letras
if len (palabra)>5:
    print("Tiene más de 5 letras")
else:
    print("Tiene 5 letras o menos")
#Comprobar si una palabra termina en:"s"
if palabra.lower().endswith("S"):
    print("La palabra si termina en s")
else:
    print("La palabra no termina con la letra s")
#Creo que el programa se puede mejorar en varios aspectos entre ellos:
#1.-poner para que la letra que se cambie sea por s en el final , pero eso en este caso particular
#2.-luego que se cambie la letra por s al final de la palabra la palabra nueva sea la que marque si o no termina en s