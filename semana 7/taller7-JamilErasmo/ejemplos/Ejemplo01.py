numero = 1
denominador = 1
contador = 1 
while contador < 5:
    if (contador % 2)== 0:
        print("%s%d/%d"%("-",numero,denominador))
    else:
        print("%s%d/%d"%("+",numero,denominador))
    contador = contador + 1  
    denominador = denominador +2   
print("\n")