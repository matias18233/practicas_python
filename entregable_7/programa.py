# FUNCIONES
def agregarItem():
    global persona
    registroAux = dict.fromkeys(encabezado, "")
    for i in encabezado:
        if i == "id":
            registroAux[i] = len(persona) + 1
        elif i == "edad" or i == "comision":
            cadena = input(f"Ingrese {i}: ")
            registroAux[i] = int(cadena)
        else:
            cadena = input(f"Ingrese {i}: ")
            registroAux[i] = cadena
    persona.append(registroAux)
    print("Se ha agregado correctamente la información")
    print()

def verItem():
    if len(persona) == 0:
        print("No hay registros para mostrar")
        return 0
    for i in encabezado:
        print(i, end="\t\t")
    print()
    for i in persona:
        for j in i.values():
            print(j, end="\t\t")
        print()
    print()

def eliminarItem():
    global persona
    print("Indique el valor de ID del registro a eliminar:")
    verItem()
    
    encontrado = False
    # Recuperamos el id del registro a eliminar
    cadena = input()
    for i in persona:
        for j in i.values():
            if j == int(cadena):
                encontrado = True
                break
        if encontrado == True:
            persona.remove(i)
            break

persona = []
encabezado = ["id", "nombre", "apellido", "comision"]

# PROGRAMA PRINCIPAL
salir = False
while salir == False:
    # Interfaz del sistema, vía consola
    print("--------------------------")
    print("Ingrese el valor de la acción seleccionada:")
    print(" 1 - Agregar")
    print(" 2 - Ver")
    print(" 3 - Eliminar")
    print(" 4 - Salir del sistema")
    
    cadena = input()

    if cadena == "1":
        agregarItem()
    elif cadena == "2":
        verItem()
    elif cadena == "3":
        eliminarItem()
    elif cadena == "4":
        salir = True
