limite = 3
contador = 1
suma_total = float(0)
print("Ingrese las notas de los estudiantes de su materia")
while contador <= limite:
    calificacion = float(input("Ingrese calificación numero %d\n" %(contador)))
    suma_total = suma_total + calificacion
    contador = contador + 1
promedio_Final = suma_total / limite
print("El promedio final es %f\n" %(promedio_Final))