cadena = input("¿Qué cantidad desea invertir?: ")
montoInvertir = float(cadena)

cadena = input("¿Cuál es el interés anual?: ")
interesAnual = float(cadena)
interesAnual = 1 + (interesAnual * 0.01)

cadena = input("Indique la cantidad de años a invertir: ")
aniosInvertir = int(cadena)

gananciaObtenida = 0
for i in range(aniosInvertir):
    gananciaObtenida += montoInvertir * interesAnual

print("La ganancia obtenida será: ", gananciaObtenida)