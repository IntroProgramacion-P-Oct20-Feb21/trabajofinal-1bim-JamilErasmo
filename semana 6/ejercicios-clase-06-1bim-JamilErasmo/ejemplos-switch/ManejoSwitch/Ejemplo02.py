valor1 = int(input("Ingrese el primer valor de la operación: "))
valor2 = int(input("Ingrese el segundo valor de la operación: "))
op=int(input("Seleccione la operación que desea realizar\n"
+"Ingrese 1 para sumar\n"
+"Ingrese 2 para restar\n"
+"Ingrese 3 para multiplicar\n"))

if op is 1:
    resultado = valor1 + valor2
    tipo = "suma"
elif op is 2:
    resultado = valor1 - valor2
    tipo = "resta"
elif op is 3:
    resultado = valor1 *valor2
    tipo = "multiplicación"
else:
    print("operación incorrecta")
print("El resultado de la operación %s es: %d\n"
%(tipo, resultado))