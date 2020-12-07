cadenaF = ""
while True:
    nota = float(input("Ingrese calificaciones: "))
    cadenaF = "%s%.2f\n" %(cadenaF, nota)

    salida = int(input("Ingrese '-111' para salir del ciclo: "))
    if salida == -111:
        break
print("Listado de notas \n%s \n"%(cadenaF))