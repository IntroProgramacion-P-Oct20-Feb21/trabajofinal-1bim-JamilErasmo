contador = 1
cadenaF = ""
while contador <= 5:
    nombre = input("Ingresar el nombre del empleado: ")
    nDias = int(input("Ingrese el número de días trabajos: "))
    cDias = float(input("Ingrese el costo del día trabajado: "))

    totalp = nDias * cDias
    cadenaF = "%s\t%s\t%d\t%.2f$\t%.2f$\n" %(cadenaF,
    nombre, nDias, cDias,totalp)
    contador = contador +1
print(cadenaF)