montoPrestamo = float(input("Ingresar el monto del préstamo: "))
interesMensual = float(input("Ingresar el interés mensual a pagar: "))

totalMensual = montoPrestamo / 12 + interesMensual
print("El valor mensual a pagar es: %.2f"%(totalMensual))