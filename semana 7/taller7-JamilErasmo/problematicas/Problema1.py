cadenaedad =""
sumaedades = 0
contadorIteraciones = 0
sumaEstaturas = 0.0
cadenaReportes = ""
cadenaReportes = "%s%s\n" %(cadenaReportes,"Listado de jugadores")
while True:
    nombreJugador = input("Ingrese el nombre del jugador: ")
    posicionCampo = input("Ingrese la posicion en el campo: ")
    edad = int(input("Ingrese la edad del jugador: "))
    estatura = float (input("Ingrese la estatura del jugador: "))

    sumaedades= sumaedades + edad
    sumaEstaturas = sumaEstaturas + estatura
    contadorIteraciones = contadorIteraciones + 1

    cadenaReportes = "%s%s.) %s -%s-, edad %d, estatura %.2f\n" %(cadenaReportes,
    contadorIteraciones, nombreJugador, posicionCampo,edad, estatura)
    cadenaedad = "%s%d\n"%(cadenaedad,edad)
    salir = input("Si desea salir del ciclo escriba 'si': ")
    if salir == "si":
        break
promedioEdad = float(sumaedades / contadorIteraciones)
promedioEstatura = sumaEstaturas / contadorIteraciones

cadenaReportes = "%sListado edades:\n%s\n Promedio edades: %.2f"%(cadenaReportes,
cadenaedad, promedioEdad)
cadenaReportes = "%s Promedio estatura: %.2f\n"%(cadenaReportes, promedioEstatura)

print("%s\n"%(cadenaReportes))