contador = 1
cadenaFinal =""
tipodeOperacion=input("Indique qué tipo de tabla quiere realizar\n"
+"suma\n"
+"o\n"
+"multiplicación: \n")
numeroTabla = int(input("Ingresar el número de tabla: \n"))
limiteTabla = int(input("Ingresar el límite de tabla: \n"))

if tipodeOperacion == "suma":
    cadenaFinal = "%s%s\n" %(cadenaFinal, "Tabla de sumar")
    while contador <= limiteTabla:
        operacion = numeroTabla + contador
        cadenaFinal = "%s%d + %d = %d\n" %(cadenaFinal, numeroTabla,
        contador, operacion)
        contador = contador + 1
elif tipodeOperacion == "multiplicación":
    cadenaFinal = "%s%s\n" %(cadenaFinal, "Tabla de multiplicar")
    while contador <= limiteTabla:
        operacion= numeroTabla * contador
        cadenaFinal = "%d%d*%d = %d\n" %(cadenaFinal, numeroTabla,
        contador, operacion)
        contador = contador + 1
else:
    cadenaFinal = "%s%s\n"%(cadenaFinal, "Error en tipo de operación") 
print("%s\n"%(cadenaFinal)) 