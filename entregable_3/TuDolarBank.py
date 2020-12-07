# Nombre: Fernando Matías
# Apellido: Cruz
# Comisión: 1

# Se obtiene la cantidad de dólares a comprar
cadena = input("Ingrese la cantidad de dólares a comprar: $")
dolarComprar = float(cadena)

if dolarComprar <= 0:
    print("No puede comprar una cantidad negativa de dólares")
else:
    # Comienza el cálculo del valor en pesos
    valorPesos = 0
    if dolarComprar < 100.00:
        valorDolar = 77.75
        valorPesos = valorDolar * dolarComprar
    elif (dolarComprar >= 100.00) and (dolarComprar <= 200.00):
        valorDolar = 101.08
        valorPesos = valorDolar * dolarComprar
    elif dolarComprar > 200.00:
        valorDolar = 137.00
        valorPesos = valorDolar * dolarComprar

    print("el importe a pagar por USD", dolarComprar, " es $ ", valorPesos)