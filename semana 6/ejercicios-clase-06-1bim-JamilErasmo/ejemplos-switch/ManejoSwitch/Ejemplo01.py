valor1 = int(input("Ingrese el primer valor de la operación: "))
valor2 = int(input("Ingrese el segundo valor de la operación: "))
op=int(input("Seleccione la operación que desea realizar\n"
+"Ingrese 1 para sumar\n"
+"Ingrese 2 para restar\n"
+"Ingrese 3 para multiplicar\n"))

if op is 1:
    resultado = valor1 + valor2
elif op is 2:
    resultado = valor1 - valor2
elif op is 3:
    resultado = valor1 *valor2
else:
    print("operación incorrecta")
print("El resultado de la operación es: %d\n"
%(resultado)) 