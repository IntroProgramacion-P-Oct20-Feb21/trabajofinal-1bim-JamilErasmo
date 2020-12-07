contador = 1
cadenaF = ""
for contador2 in range(1,8):
    if (contador % 2)== 0:
        contador = contador + 1
        cadenaF = "%s +1/%d"%(cadenaF, contador)
    else:
        contador = contador + 2 
        cadenaF = "%s -1/%d"%(cadenaF, contador)
    contador2 = contador2 + 1
    contador = contador + 1
print("1 %s"%(cadenaF))  