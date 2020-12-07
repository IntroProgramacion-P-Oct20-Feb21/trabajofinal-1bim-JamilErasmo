preciocpu = float(input("Ingresar el precio del cpu: "))
precioteclado = float(input("Ingresar el precio del teclado: "))
preciopantalla = float(input("Ingresar el precio de la pantalla: "))
precioraton = float(input("Ingresar el precio del raton: "))

total = preciocpu + preciopantalla + precioraton + precioteclado
print("El valor total a pagar por la computadora es: %.2f$"%(total))