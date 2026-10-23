#Programa que me indica como me fue en el parcial y que me dira mi mamá
print("CALIFICACIONES")
calif=float(input("¿Cuál fue tu calificación?:"))
if calif==10:
    print("¡¡¡EXCELENTE!!!")
elif calif==9:
    print("¡¡¡MUY BIEN!!!")
elif calif==8:
    print("¡¡¡BIEN!!!")
elif calif==7:
    print("¡¡¡PUEDES MEJORAR!!!")
elif calif==6:
    print("¡¡¡HAY MIJO!!!")
else:
    print("¡¡¡CHANCLAZOOOOOOO!!!")
#Programa que me indica que tanta calor hace
print("TEMPERATURA")
temp=float(input("¿A que temperatura estas?:"))
if temp>=40:
    print("¡HACE MUCHA CALOR!")
elif temp>=30 and temp<40:
    print("¡ESTA TEMPLADITO!")
elif temp>=20 and temp<30:
    print("¡ESTA FRESCO")
elif temp<20:
    print("¡HACE FRÍO!")
else:
    print("¡NO VALIDO!")
#Programa que solicita sexo y edad para sacar la cartilla militar
print("CARTILLA MILITAR")
sexo=input("¿Eres hombre o mujer?:")
edad=int(input("Ingresa tu edad actual:"))
if sexo=="hombre" and edad>=18:
    print("¡Puedes sacar cartilla militar!")
else:
    print("¡No puedes sacar cartilla militar!")