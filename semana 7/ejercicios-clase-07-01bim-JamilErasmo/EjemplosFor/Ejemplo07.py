for i in range(1,21,1):
    print("Tabla de multiplicar del número %d\n"%(i))
    for contador in range(1,10,1):
        operación = i * contador 
        print("%d x %d = %d\n"%(i, contador, operación,))
    print("\n")