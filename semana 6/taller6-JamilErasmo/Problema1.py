netflix = float (10)
disney = float (6)
apple = float (5)
amazon = float (4.50)
bandera = True
usuario =input("Ingresar el nombre del usuario\n")
while bandera:
    empresa = input("Ingrese el nombre de la empresa: \nNetflix\n"
    +"Disney\n"
    +"Apple\n"
    + "Amazon\n")
    if empresa == "Netflix":
        impuesto = (netflix * 10)/100
        total = netflix + impuesto
        print("Usuario: %s\nEmpresa: %s\n Precio base: %.2f\n Impuesto: %.2f\nTotal a pagar es: %.2f" %(usuario,
        empresa, netflix, impuesto, total))
    elif empresa == "Disney":
        impuesto = (disney * 10)/100
        total = disney + impuesto
        print("Usuario: %s\nEmpresa: %s\n Precio base: %.2f\n Impuesto: %.2f\nTotal a pagar es: %.2f" %(usuario,
        empresa, disney, impuesto, total))
    elif empresa == "Apple":
        impuesto = (apple * 10)/100
        total = apple + impuesto
        print("Usuario: %s\nEmpresa: %s\n Precio base: %.2f\n Impuesto: %.2f\nTotal a pagar es: %.2f" %(usuario,
        empresa, apple, impuesto, total))
    elif empresa == "Amazon":
        impuesto = (amazon * 10)/100
        total = amazon + impuesto
        print("Usuario: %s\nEmpresa: %s\n Precio base: %.2f\n Impuesto: %.2f\nTotal a pagar es: %.2f" %(usuario,
        empresa, amazon, impuesto, total))
    negacion= int(input("Ingrese -1 para salir de la secuencia: "))
    if negacion == -1:
        bandera = False