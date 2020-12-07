porcentaje = float (10) 
cantidadR = float (input("Ingresar la cantidad requerida: "))
preciouni = float (input("Ingresar el valor unitario: "))

total = float (preciouni * cantidadR)
if cantidadR > 50:
    descuento =( total * porcentaje)/100
    total = total - descuento
print("El valor total a pagar es: %.2f$" %(total))