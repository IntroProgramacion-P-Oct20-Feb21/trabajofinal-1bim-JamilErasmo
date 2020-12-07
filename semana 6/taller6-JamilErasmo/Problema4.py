contador = 1
cadenaF = ""
while contador <= 10 :
    nombre = input("Ingrese el nombre del jugador: ")
    cpuntos = int(input("Ingrese la cantidad de puntos anotados: "))
    cfaltas = int(input("Ingrese la cantidad de faltas cometidas: "))
    contador = contador + 1
    cadenaF = "%s\t%s\t%d\t%d\n" %(cadenaF, nombre, cpuntos, cfaltas)
print(cadenaF)