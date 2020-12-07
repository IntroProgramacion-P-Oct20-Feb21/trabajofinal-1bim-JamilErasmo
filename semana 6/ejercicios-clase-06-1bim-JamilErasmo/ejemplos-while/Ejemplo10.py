limite_tabla = 12
contador = 1
cadena = ""
tabla = int(input("Ingresar el número de la tabla a generar: "))
while contador <= 12:
    operacion = tabla * contador
    cadena = "%s%d * %d = %d\n" %(cadena, tabla, contador, operacion)
    contador = contador + 1