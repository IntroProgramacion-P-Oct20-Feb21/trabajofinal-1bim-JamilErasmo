contador= 1 
cadenaF = ""
while contador <=4:
    nombre = input("Ingresar el nombre del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    if promedio >=7:
        cadenaF = "%s\t%s\t%.2f\t%s\n" %(cadenaF, nombre, promedio, "Aprobado")
    else:
        cadenaF = "%s\t%s\t%.2f\t%s\n" %(cadenaF, nombre, promedio, "Reprobado")
    contador = contador +1    
print(cadenaF)