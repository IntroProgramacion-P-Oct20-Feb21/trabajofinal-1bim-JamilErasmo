contador = 1
tabla = int(input("Ingrese la tabla a generar: "))
while True:
    operacion = tabla * contador
    print( "%d * %d = %d\n" %(tabla, contador, operacion))
    contador = contador + 1 
    if (contador >= 10):
        break