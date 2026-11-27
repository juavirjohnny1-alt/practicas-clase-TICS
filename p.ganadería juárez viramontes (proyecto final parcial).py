#PROGRAMA DEL REGISTRO DE UNA GANADERÍA
print("GANADERÍA JUÁREZ VIRAMONTES")
print("BIENVENIDO")
#RF1 CONTRASEÑA DE SEGURIDAD
contraseña=301412
password=int(input("Ingresa la contraseña de seguridad: "))
if (password==contraseña):
    print("Bienvenido a Ganadería Juárez Viramontes")
    #RF2 MENÚ DEL PROGRAMA
    ganados=[]
    while True:
        print("MENÚ")
        print("1.-Registrar ganado")
        print("2.-Dar de baja por venta")
        print("3.-Modificar registro del ganado")
        print("4.-Ver información de un solo bovino registrado (mediante núm arete)")
        print("5.-Buscar ganado")
        print("6.-Registro completo del ganado")
        print("7.-Registro del ganado por corral")
        print("8.-Cantidad de ganado registrado (en número)")
        print("9.-Organizar el ganado en base al sexo (corral 1 y 2)")
        print("10.-Salir")
        opcion=int(input("Selecciona una opción: "))
        #RF3 REGISTRAR GANADO
        if opcion==1:
            print("Registrar ganado:")
            cantidad=int(input("¿Cuántos bovinos deseas registrar?: "))
            for i in range (cantidad):
                print("Bovino",i + 1)
                ganado={
                    "Peso":float(input("Ingresa el peso de el bovino: ")),
                    "Color":input("Ingresa el color de el bovino: "),
                    "Arete":int(input("Ingresa el número de arete de el bovino: ")),
                    "Provenencia":input("Ingresa el lugar de provenencia de el bovino : "),
                    "Dueño anterior":input("Ingresa el nombre del dueño anterior de el bovino: "),
                    "Sexo":input("Ingresa el sexo de el bovino: "),
                    "Corral":int(input("Ingresa el número del corral al que va designado el bovino (1 o 2): "))
                }  
                ganados.append(ganado)
                print("Bovino registrado correctamente")
        #RF4 DAR DE BAJA POR VENTA DE GANADO (MEDIANTE EL NÚMERO DE ARETE)
        elif opcion==2:
            print("Dar de baja por venta:")
            bovinoVendido=int(input("Ingresa el número de arete de el bovino que se vendio: "))
            for bovino in ganados:
                if bovino["Arete"]==bovinoVendido:
                    print("Información de el bovino")
                    print(bovino)
                    vender=input("¿Quieres vender este bovino? (si/no): ")
                    if vender=="si":
                        ganados.remove(bovino)
                        print("Bovino vendido")
                    else:
                        print("Bovino no vendido")
                    break
            else:
                print("No existe ningun bovino registrado con ese arete")
        #RF5 MODIFICAR REGISTRO DEL GANADO EN CASO DE QUE ESTE MAL AGREGADO
        elif opcion==3:
            print("Modificar registro del ganado:")
            bovinoModificar=int(input("Ingresa el número de arete de el bovino a modificar: "))
            for bovino in ganados:
                if bovino["Arete"]==bovinoModificar:
                    print("Bovino encontrado, ingresa los nuevos datos que se han necesarios: ")
                    bovino["Peso"]=float(input("Ingresa peso de el bovino: "))
                    bovino["Color"]=input("Ingrese el color de el bovino: ")
                    bovino["Arete"]=int(input("Ingresa el número de arete de el bovino (deberia de ser igual): "))
                    bovino["Provenencia"]=input("Ingresa el lugar de provenencia de el bovino: ")
                    bovino["Dueño anterior"]=input("Ingresa el nombre de el dueño anterior de el bovino: ")
                    bovino["Sexo"]=input("Ingresa el sexo de el bovino: ")
                    bovino["Corral"]=int(input("Ingresa el número del corral de el bovino(1 o 2):"))
                    print("Datos del bovino mofificados")
                    break
            else:
                 print("No existe ningun bovino registrado con ese número de arete")
        #RF6 VER LA INFORMACIÓN DE UN SOLO BOVINO REGISTRADO, MEDIANTE EL NÚMERO DE ARETE
        elif opcion==4:
            print("Ver información de un solo bovino registrado (mediante núm arete):")
            areteInformacion=int(input("Ingresa el número de arete, del bovino que desea saber sus datos: "))
            for bovino in ganados:
                if bovino["Arete"]==areteInformacion:
                    print("Información de el bovino: ")
                    for clave, valor in bovino.items():
                        print(f"{clave}:{valor}")
                    break
            else:
                print("No existe ningun bovino registrado con ese número de arete")
        #RF7 BUSCAR GANADO
        elif opcion==5:
            print("Buscar ganado:")
            areteBuscar=int(input("Ingresa el número de arete, de el bovino que deseas saber si está en el sistema: "))
            for bovino in ganados:
                if bovino["Arete"]==areteBuscar:
                    print("Si se encuentra en el registro este bovino")
                    break
            else:
                print("No se encuentra en el registro este bovino")
        #RF8 REGISTRO COMPLETO DEL GANADO
        elif opcion==6:
            print("Registro completo del ganado:")
            for i in range (len(ganados)):
                print(f"Bovino {i + 1}:")
                for clave, valor in ganados[i].items():
                    print(f"{clave}:{valor}")
        #RF9 REGISTRO POR CORRAL DEL GANADO
        elif opcion==7:
            print("Registro del ganado por corral:")
            numeroCorral=int(input("Ingresa el número del corral, para saber el registro de bovinos de este corral: "))
            if numeroCorral==1 or numeroCorral==2:
                print("Registro de el ganado del corral", numeroCorral)
                corralVacio=True
                for i in range(len(ganados)):
                    if ganados[i]["Corral"]==numeroCorral:
                        corralVacio=False
                        print(f"Bovino {i + 1}:")
                        for clave, valor in ganados[i].items():
                            print(f"{clave}:{valor}")
                if corralVacio==True:
                    print("0")
            else:
                print("No existe este corral")
        #RF10 CANTIDAD DE GANADO REGISTRADOS (EN NÚMERO)
        elif opcion==8:
            print("Cantidad de ganado registrado (en número):")
            print("Se cuenta con un registro total de", len(ganados))
        #RF11 ORGANIZAR EL GANADO MEDIANTE (SEXO EN CORRAL 1 Y 2)
        elif opcion==9:
            print("Organizar el ganado en base al sexo (corral 1 y 2):")
            corral1=[] #MACHOS
            corral2=[] #HEMBRAS
            for bovino in ganados:
                if bovino["Sexo"].lower() in ["macho", "m"]:
                    corral1.append(bovino)
                elif bovino["Sexo"].lower() in ["hembra", "h"]:
                    corral2.append(bovino)
                else:
                    print("El bovino no es ni macho ni hembra")
            print("Corral 1 (MACHOS)")
            for i in range(len(corral1)):
                print(f"Bovino {i + 1}:")
                for clave, valor in corral1[i].items():
                    print(f"{clave}:{valor}")
            print("Corral 2 (HEMBRAS)")
            for i in range(len(corral2)):
                print(f"Bovino {i + 1}:")
                for clave, valor in corral2[i].items():
                    print(f"{clave}:{valor}")
        #RF12 SALIR DEL SISTEMA
        elif opcion==10:
            print("Salir:")
            print("Gracias, hasta luego")
            print("Saliendo del programa.....")
            break
        else:
            print("Selecciona una opción que si este en el menú")
else:
    print("Contraseña Incorrecta, sigue intentando")
