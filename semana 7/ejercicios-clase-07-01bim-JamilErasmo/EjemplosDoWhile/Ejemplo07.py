contador = 1
cadenaF = ""
while True:
    cadenaF = "%s Tabla de mulltiplicar del %d\n" %(cadenaF, contador)
    for i in range (1,11) :
        operacion = i * contador
        cadenaF = (" %s%d x %d = %d\n" %(cadenaF, contador, i, operacion))
    cadenaF = "%s\n" %(cadenaF)
    contador = contador + 1 
    if contador >= 6:
        break
print("%s" %(cadenaF))