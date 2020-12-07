largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingresar el ancho del terreno: "))
costoMetro = float(input("Ingrese el costo del metro cuadrado: "))
nombre = input("Ingrese el nombre del comprador: ")

area = largo * ancho
costoTerreno = area * costoMetro

print("El costo del terreno es: %.2f\nEl compradpr es: %s\n" %( costoTerreno,
nombre))