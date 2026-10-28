#PROGRAMA DE PARENTESCO FAMILIAR
print("PARENTESCO FAMILIAR")
parentesco=input("¿Qué eres mio?:")
if parentesco=="hermano" or parentesco=="hijo":
    print("!Eres de mi familia¡")
else:
    print("!No eres de mi familia¡")
#PROGRAMA DE EDAD PARA UN CONCIERTO
print("EDAD PARA UN CONCIERTO")
edad=int(input("Qué edad tienes:"))
permiso=input("¿Tienes permiso dado po tus padres para ir?:")
acompañado=input("¿Vas a ir acompañado al concierto?:")
if edad>=18 or permiso=="si":
    print("Puedes entrar al concierto")
elif edad>=18 or acompañado=="si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")