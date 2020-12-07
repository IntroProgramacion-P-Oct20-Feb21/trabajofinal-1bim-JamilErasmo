porcentajeAl = float (20)
porcentajeJap = float (30)
porcentajeIta = float (15)
porcentajeUs = float (8)
marca = input("Ingresar la marca del automóvil: ")
origen = input("Ingresar el origen del automóvil: ")
costo = float (input("Ingresar el costo del automóvil: "))

if origen == "Japon":
    impuesto = (costo * porcentajeJap)/100
    total = costo + impuesto
else:
    if origen == "Italia":
        impuesto = (costo * porcentajeIta)/100
        total = costo + impuesto
    else:
        if origen == "USA":
            impuesto = (costo * porcentajeUs)/100
            total = costo + impuesto
        else:
            print("El origen del vehículo no es válido ")   

print("El valor del impuesto total a pagar : %.2f\nEl valor total de venta es: %.2f" %(impuesto, total))