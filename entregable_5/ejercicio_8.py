cadena = input("Ingrese un anio: ")
anio1 = int(cadena)

cadena = input("Ingrese otro anio: ")
anio2 = int(cadena)

for anio in range(anio1, anio2 + 1):
    if anio % 4 == 0 and anio % 100 != 0:
        print("Es bisiesto", anio)
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        print("Es bisiesto", anio)