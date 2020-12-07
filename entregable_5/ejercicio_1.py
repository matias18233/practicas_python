# < 40 horas = +50%

# Obtenemos el costo de una hora trabajada
cadena = input("Ingrese el valor de cada hora: $ ")
valorHoraTrabajada = float(cadena)

# Obtenemos las horas trabajadas por el empleado
cadena = input("Ingrese las horas trabajadas por el empleado: ")
horasTrabajadas = int(cadena)

sueldo = 0
if horasTrabajadas < 40:
    sueldo = valorHoraTrabajada * horasTrabajadas
else:
    sueldo = valorHoraTrabajada * 40
    for hora in range(41, horasTrabajadas + 1):
        print("Hora actual:", hora)
        sueldo = sueldo + (valorHoraTrabajada * 1.50)
print(sueldo)