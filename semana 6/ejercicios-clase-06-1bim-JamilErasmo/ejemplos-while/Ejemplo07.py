suma_total = float(0)
contador = 0
bandera = True
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
    calificacion = float(input("Ingrese calificacion: "))
    suma_total = suma_total + calificacion
    contador = contador + 1
    temporal = int(input("Ingrese el valor -1 para salir del ciclo: "))
    if temporal == -1:
        bandera = False
promedio_final = float (suma_total / contador)       
print("El promedio final es:  %.2f\n"%(promedio_final))