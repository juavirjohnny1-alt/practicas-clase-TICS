#PROGRAMA DEL REGISTRO DE UNA GANADERÍA
print("GANADERÍA JUÁREZ VIRAMONTES")
print("BIENVENIDO")
#RF1 CONTRASEÑA DE SEGURIDAD
contraseña=301412
password=int(input("Ingresa la contraseña de seguridad: "))
if (password==contraseña):
    print("Bienvenido a Ganadería Juárez Viramontes")
else:
    print("Contrasena Incorrecta, sigue intentando")

#RF2 MENÚ DEL PROGRAMA
print("MENÚ")
while True:
    print("1.-Registrar ganado")
    print("2.-Dar de baja por venta")
    print("3.-Modificar registro del ganado")
    print("4.-Ver información del ganado (unitario mediante núm arete)")
    print("5.-Busar ganado")
    print("6.-Registro completo del ganado")
    print("7.-Registro del ganado por corral")
    print("8.-Cantidad de ganado registrado (en número)")
    print("9.-Organizar el ganado en base al sexo")
    print("10.-Salir")
    opcion=int(input("Selecciona una opción: "))
    #RF3 REGISTRAR GANADO
    if opcion==1:
        ganados=[]
        cantidad=int(input("¿Cuántos bovinos deseas registrar?: "))
        for i in range (cantidad):
            print("Bovino",i +1)
            ganado={
                "peso":float(input("Ingresa el peso del bovino: ")),
                "color":input("Ingresa el color del bovino: "),
                "arete":int(input("Ingresa el número de arete del bovino: ")),
                "provenencia":input("Ingresa el lugar de provenencia y el dueño anterior del bovino: "),
                "sexo":input("Ingresa el sexo del bovino: "),
                "corral":int(input("Ingresa el número del corral al que va designado: "))
            }  
    #RF4 DAR DE BAJA POR VENTA DE GANADO(MEDIANTE EL ARETE)
    elif opcion==2:
        bovinoVendido=int(input("Ingresa el número de arete del bovino que se vendio: "))
        for bovino in ganados:
            if bovino["arete"]==bovinoVendido:
                ganados.remove(bovino)
                print("Bovino eliminado")
            else:
                print("No existe ningun bovino registrado con ese arete")
    #RF5 MODIFICAR REGISTRO DEL GANADO EN CASO DE QUE ESTE MAL AGREGADO
    elif opcion==3:
        bovinoModificar=int(input("Ingresa el número de arete del bovino a modificar: "))
        if bovino["arete"]==bovinoModificar:
            print("Bovino encontrado, ingresa los nuevos datos que se han necesarios: ")
            bovino["peso"]=float(input("Ingresa el nuevo peso del bovino: "))
            bovino["color"]=input("Ingrese el nuevo color del bovino: ")
            bovino["arete"]=int(input("Ingresa el nuevo número de arete del bovino: "))
            bovino["provenencia"]=input("Ingresa el nuevo lugar de provenencia y el dueño anterior del bovino: ")
            bovino["sexo"]=input("Ingresa el nuevo sexo del bovino: ")
            bovino["corral"]=int(input("Ingresa el nuevo número del corral del bovino:"))
            print("Datos del bovino mofificados")
        else:
            print("No existe ningun bovino registrado con ese número de arete")
    #RF6 VER LA INFORMACIÓN DE UN SOLO BOVINO REGISTRADO, MEDIANTE EL NÚMERO DE ARETE
    elif opcion==4:
        areteBuscarSolo=int(input("Ingresa el número de arete, del bovino que desea saber sus datos: "))
        for bovino in ganados:
            if bovino["arete"]==areteBuscarSolo:
                print("Información del bovino: ")
                print(bovino)
            else:
                print("No existe un bovino registrado con ese número de arete")