suma_total = float(0)
bandera = True
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
    calificacion = float(input("Ingrese calificacion: "))
    suma_total = suma_total + calificacion
    temporal = input("Ingrese 'Si' para salir del ciclo: ")
    if temporal == "Si":
        bandera = False
print("Suma de calificaiones es %.2f\n"%(suma_total))