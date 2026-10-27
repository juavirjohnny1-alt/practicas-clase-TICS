#PROGRAMA APOYO A FAMILIAS
print("APOYO A FAMILIAS")
sexo=input("¿De que tipo de sexo eres?:")
edad=int(input("¿Cuál es tu edad?:"))
estadoCivil=input("¿Cuál es tru estado cívil?:")
cantidadDeHijos=int(input("¿Cuantos hijos tienes?:"))

if sexo==("mujer") and cantidadDeHijos==1 and edad<18:
    print("Eres mujer, tienes un hijo y eres menor de edad entonces el apoyo será de $800")
elif sexo==("mujer") and cantidadDeHijos==1 and edad>=18:
    print("Eres mujer, tienes un hijo y eres mayor de edad entonces el apoyo será de $300")
elif sexo==("mujer") and cantidadDeHijos>1 and edad<18:
    print("Eres mujer, tienes más de un hijo y eres menor de edad entonces el apoyo será de $1500")
elif sexo==("mujer") and cantidadDeHijos>1 and edad>=18:
    print("Eres mujer, tienes más de un hijo y ya eres mayor de edad entonces el apoyo es de $500")
elif sexo==("hombre") and cantidadDeHijos>=1 and estadoCivil==("soltero"):
    print("Eres hombre y tienes hijos el apyo es de $780")
else:
    print("No válido")