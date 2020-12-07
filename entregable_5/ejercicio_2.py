# 300.000 -> 300 km
# 300.000 + (15.000 x km) -> 300 km - 1000 km
# 300.000 + (10.000 x km) -> 1001 km

# Obtenemos los kilómetros recorridos
cadena = input("Ingrese los kilómetros recorridos: ")
kilometrosRecorridos = int(cadena)

costoTotal = 0
if kilometrosRecorridos < 300:
    costoTotal = 300000.00
elif (kilometrosRecorridos > 300) and (kilometrosRecorridos < 1000):
    costoTotal = 300000.00
    for kilometro in range(301, kilometrosRecorridos + 1):
        costoTotal = costoTotal + 15000
elif kilometrosRecorridos > 1000:
    costoTotal = 300000.00
    for kilometro in range(1001, kilometrosRecorridos + 1):
        costoTotal = costoTotal + 10000

print("El monto a abonar es de: $", costoTotal)