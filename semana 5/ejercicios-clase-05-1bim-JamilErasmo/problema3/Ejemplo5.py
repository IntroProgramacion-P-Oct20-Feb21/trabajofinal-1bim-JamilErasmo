porcentaje1 = float (10)
porcentaje2 = float (15)
porcentaje3 = float (20)
numeroDias = float(input("Ingresar el número de días que se hospedará: "))
precioHabitacion = float(input("Ingresar el valor diario de la habitación: "))
if (numeroDias > 5) & (numeroDias <= 10):
    subtotal = numeroDias * precioHabitacion
    descuento = (porcentaje1 * subtotal)/100
    valorTotal = subtotal - descuento
else:
    if (numeroDias > 10) & (numeroDias <= 15):
        subtotal = numeroDias * precioHabitacion
        descuento = (porcentaje2 * subtotal)/100
        valorTotal = subtotal - descuento
    else:
        if numeroDias > 15:
            subtotal = numeroDias * precioHabitacion
            descuento = (porcentaje3 * subtotal)/100
            valorTotal = subtotal - descuento


print("El valor subtotal es: %.2f  El descuento es: %.2f\n El valor total a pagar es: %.2f\n"
%(subtotal,descuento,valorTotal))  