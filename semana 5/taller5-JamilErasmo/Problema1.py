porcentaje = float(10)
costoK = float(input("Ingresar el costo de kilovatios por hora: "))
consumidosK = float(input("Ingresar el total de kilovatios consumidos al mes: "))
edad = int(input("Ingresar la edad del usuario: "))

total = costoK * consumidosK
if edad > 65:
    descuento = (total * porcentaje)/100
    total = total - descuento 

print("El valor total a pagar es: %.2f" %(total))