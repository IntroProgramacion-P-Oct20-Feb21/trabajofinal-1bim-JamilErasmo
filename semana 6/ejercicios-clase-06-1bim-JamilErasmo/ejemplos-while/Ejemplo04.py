limite_inferior = 10
limite_superior = 20
suma = 0
contador = 10 
while (contador >= limite_inferior) & (contador <= limite_superior):
    suma = suma + contador
    print("contador %d\n"%(contador))
    contador = contador + 5
print("La suma final es: %d\n" %(suma))