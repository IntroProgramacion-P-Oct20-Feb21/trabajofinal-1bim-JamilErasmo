tabla = int (input("Ingrese el número de tabla que desea generar: "))
for contador in range (5,31,1):
    operacion = tabla * contador
    print("%d x %d = %d\n"%(tabla, contador, operacion))