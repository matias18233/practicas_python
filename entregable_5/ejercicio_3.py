import datetime, time

# Obtenemos la hora de corte (20 segundos después)
horaCorteLlamada = datetime.datetime.now() + datetime.timedelta(seconds=20)

contador = 1
costoLlamada = 0
while horaCorteLlamada > datetime.datetime.now():
    print("Hora actual:", datetime.datetime.now())
    if contador <= 5:
        costoLlamada = costoLlamada + 1.00
    elif contador <= 8:
        costoLlamada = costoLlamada + 0.80
    elif contador <= 10:
        costoLlamada = costoLlamada + 0.70
    else:
        costoLlamada = costoLlamada + 0.50
    print("Costo actual: $", costoLlamada)
    time.sleep(1)
    contador = contador + 1
