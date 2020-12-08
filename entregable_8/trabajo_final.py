# Nombre: Fernando Matías
# Apellido: Cruz
# Comisión: 1

from random import randrange

# Permite obtener un número de ID único (en un rango que va del 0 al 100)
def obtenerIndice():
    global productos
    control = False
    while control == False:
        indice = randrange(100)
        repetido = False
        if len(productos) == 0:
            control = True
        else:
            for i in productos:
                for j in i.values():
                    if j == indice:
                        repetido = True
                        break
                    else:
                        break
                if (repetido == True):
                    break
            if repetido == False:
                control = True
    return indice

# Permite agregar nuevos productos
def agregarProducto():
    global productos
    productosAux = dict.fromkeys(encabezadosProd, "")
    for i in encabezadosProd:
        if i == "id":
            productosAux[i] = obtenerIndice()
        elif i == "stock":
            cadena = input(f"Ingrese {i}: ")
            productosAux[i] = int(cadena)
        else:
            cadena = input(f"Ingrese {i}: ")
            productosAux[i] = cadena
    productos.append(productosAux)
    print("- Se ha agregado correctamente el producto -")
    print()

# Permite mostrar todos los productos existentes
def verProducto():
    if len(productos) == 0:
        print("- No hay registros para mostrar -")
        return 0
    for i in encabezadosProd:
        print(i, end="\t\t")
    print()
    for i in productos:
        for j in i.values():
            print(j, end="\t\t")
        print()
    print()

# Permite eliminar los productos existentes (incluidas sus promociones)
def eliminarProducto():
    global productos
    print("Indique el valor de ID del registro a eliminar:")
    verProducto()
    encontrado = False
    cadena = input() # Recuperamos el id del registro a eliminar
    for i in productos:
        for j in i.values():
            if j == int(cadena):
                encontrado = True
                eliminarPromocion(int(cadena))
                break
        if encontrado == True:
            productos.remove(i)
            break
    print("- Se ha eliminado correctamente el producto -")
    print()

# Permite agregar una promoción a los productos existentes
def agregarPromocion():
    global productos
    print("Indique el valor de ID del registro a agregarle una promoción:")
    verProducto()
    encontrado = False
    salir = False
    indiceEncontrado = ""
    precioEncontrado = ""
    nombreEncontrado = ""
    cadena = input() # Recuperamos el id y precio del registro que le cargaremos un precio de promoción
    for i in productos:
        index = 0
        for j in i.values():
            if (index == 0) and (j == int(cadena)):
                indiceEncontrado = j
                encontrado = True
            elif (index == 1) and (encontrado == True):
                nombreEncontrado = j
            elif (index == 2) and (encontrado == True):
                precioEncontrado = j
                salir = True
            if salir == True:
                break
            else:
                index = index + 1
        if salir == True:
                break
    promocionAux = dict.fromkeys(encabezadosProm, "")
    for i in encabezadosProm:
        if i == "id":
            promocionAux[i] = indiceEncontrado
        elif i == "nombre":
            promocionAux[i] = nombreEncontrado
        elif i == "precio":
            promocionAux[i] =  ((85 * float(precioEncontrado)) / 100)
    promociones.append(promocionAux)
    print("- Se ha agregado correctamente la promoción -")
    print()

# Permite mostrar todas las promociones existentes
def verPromocion():
    if len(promociones) == 0:
        print("- No hay registros para mostrar -")
        return 0
    for i in encabezadosProm:
        print(i, end="\t\t")
    print()
    for i in promociones:
        for j in i.values():
            print(j, end="\t\t")
        print()
    print()
    
    pass

# Permite eliminar las promociones existentes
def eliminarPromocion(index):
    global productos
    print("Indique el valor de ID del registro a eliminar:")
    verProducto()
    
    encontrado = False
    # Recuperamos el id del registro a eliminar
    cadena = index
    for i in promociones:
        for j in i.values():
            if j == cadena:
                encontrado = True
                break
        if encontrado == True:
            promociones.remove(i)
            break
    print("- Se ha eliminado correctamente la promoción -")
    print()

# Permite cargar automáticamente productos y promociones en el sistema
def cargaAutomatica():
    print("Carga automática de productos")

# Permite realizar una venta
def realizarVenta():
    print("realizar venta")

# Permite mostrar todas las ventas existentes
def verVentas():
    print("ver ventas")

productos = []
encabezadosProd = ["id", "nombre", "precio", "stock"]
promociones = []
encabezadosProm = ["id", "nombre", "precio"]
ventas = []
encabezadosVentas = ["id", "nombre", "precio", "cantidad"]

salir = False
while salir == False:
    print("--------------------------------------")
    print("Ingrese el valor correspondiente a la opción seleccionada:")
    print(" 1 - Agregar producto")
    print(" 2 - Ver productos")
    print(" 3 - Eliminar productos")
    print(" 4 - Agregar promoción")
    print(" 5 - Ver promoción")
    print(" 6 - Eliminar promoción")
    print(" 7 - Cargar automática (prod. y promos)")
    print(" 8 - Realizar venta")
    print(" 9 - Ver ventas realizadas")
    print(" 10 - Salir del programa")

    cadena = input()
    if cadena == "1":
        agregarProducto()
    elif cadena == "2":
        verProducto()
    elif cadena == "3":
        eliminarProducto()
    elif cadena == "4":
        agregarPromocion()
    elif cadena == "5":
        verPromocion()
    elif cadena == "6":
        print("Indique el valor de ID del registro a eliminar:")
        verPromocion()
        cadena = input()
        eliminarPromocion(int(cadena))
    elif cadena == "7":
        cargaAutomatica()
    elif cadena == "8":
        realizarVenta()
    elif cadena == "9":
        verVentas()
    elif cadena == "10":
        salir = True