limite_tabla = 12
contador = 1
tabla = int(input("Ingresar el número de la tabla a generar: "))
cadena = ""
while contador <= 12:
    operacion = tabla * contador
    print("%s%d * %d = %d\n" %(cadena, tabla, contador, operacion))
    contador = contador +1