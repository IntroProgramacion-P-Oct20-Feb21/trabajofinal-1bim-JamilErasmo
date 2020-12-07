contador = 1
contador1 = 20
contador2 = 10
while contador <= 6:
    if (contador % 2)== 0 :
        print(contador ,"/", contador1)
        contador1 = contador1 + 1
    else:
        print(contador , "/" , contador2)
        contador2 = contador2 + 1
    contador = contador + 1