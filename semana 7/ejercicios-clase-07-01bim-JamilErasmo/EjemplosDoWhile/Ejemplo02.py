contador = 0
sumat = 0
cadenaF = ""
while True:
    nota = float(input("Ingresar calificacion: "))
    cadenaF = "%s%.2f\n" %(cadenaF, nota)
    sumat = sumat + nota
    salida = input("Si desea salir del cilo ingrese 'Si' o 'S': ")
    contador = contador + 1
    if (salida == "S") or (salida =="Si"):
        break
promedio = float(sumat / contador)
print("Listado de Notas:\n%s\nPromedio:\n%.2f" %(cadenaF, promedio))