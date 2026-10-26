#PROGRAMA DE BONOS DE EMPLEADOS
print("BONOS DE LOS EMPLEADOS")
print("HOLA BIENVENIDO")
nombreDelEmpleado=input("Ingresa tu nombre:")
pagoPorHora=int(input("¿Cuál es tu pago por hora?:"))
horasTrabajadas=int(input("¿Cuantas horas trabajas al mes?:"))
sueldo=(pagoPorHora*horasTrabajadas)
print("Tu sueldo mensual es de:", sueldo)
print("!!Se esta agregando un bono por horas trabajadas¡¡¡")
if sueldo>=100 and sueldo<=300:
    bono=500
    print("Tu bono es de$500")
elif sueldo>300 and sueldo<=1500:
    bono=1700
    print("Tu bono es de $1700")
elif sueldo>1500 and sueldo<=3000:
    bono=3500
    print("Tu bono es de $3500")
elif sueldo>3000 and sueldo<=8000:
    bono=8500
    print("Tu bono es de $8500")
elif sueldo>8000:
    bono=10000
    print("Tu bono es de $10000")
else:
    print("No válido no lo alcanzas")
sueldoConBono=sueldo+bono
print("Tu sueldo con bono es de:",sueldoConBono)
print("GRACIAS")