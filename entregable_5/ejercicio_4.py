from datetime import datetime, timedelta

cadena = input("Ingrese una fecha (DD/MM/AAAA): ")
fechaIngresada = datetime.strptime(cadena, '%d/%m/%Y')

# Día anterior al ingresado
fechaAnterior = fechaIngresada + timedelta(days=-1)
print("La fecha anterior es:", fechaAnterior)
# Día posterior al ingresado
fechaSiguiente = fechaIngresada + timedelta(days=+1)
print("La fecha siguiente es:", fechaSiguiente)

# Último día del mes y cuántos días faltan para dicha fecha
mesIngresado = fechaIngresada.strftime('%m')

cantidadDias = 0
control = True
fechaNueva = fechaIngresada
while control == True:
    fechaNueva = fechaNueva + timedelta(days=+1)
    mesNuevo = fechaNueva.strftime('%m')
    if mesNuevo == mesIngresado:
        cantidadDias = cantidadDias + 1
    else:
        fechaNueva = fechaNueva + timedelta(days=-1)
        control = False

print("Último día del mes:", fechaNueva)
print("Cantidad de días faltantes:", cantidadDias)