# Nombre: Fernando Matías
# Apellido: Cruz
# Comisión: 1

# Lista 1 = productos (id, nombre, precio, stock)
# Lista 2 = promociones (id, precio)

# Opciones producto: cargar, ver, eliminar
# Opciones promociones: cargar, ver, eliminar

def agregarProducto():
    global productos
    productosAux = dict.fromkeys(encabezadosProd, "")
    for i in encabezadosProd:
        if i == "id":
            productosAux[i] = len(productos) + 1
        elif i == "stock":
            cadena = input(f"Ingrese {i}: ")
            productosAux[i] = int(cadena)
        else:
            cadena = input(f"Ingrese {i}: ")
            productosAux[i] = cadena
    productos.append(productosAux)
    print("Se ha agregado correctamente la información")
    print()
    

def verProducto():
    if len(productos) == 0:
        print("No hay registros para mostrar")
        return 0
    for i in encabezadosProd:
        print(i, end="\t\t")
    print()
    for i in productos:
        for j in i.values():
            print(j, end="\t\t")
        print()
    print()

def eliminarProducto():
    global productos
    print("Indique el valor de ID del registro a eliminar:")
    verProducto()
    
    encontrado = False
    # Recuperamos el id del registro a eliminar
    cadena = input()
    for i in productos:
        for j in i.values():
            if j == int(cadena):
                encontrado = True
                break
        if encontrado == True:
            productos.remove(i)
            break

def agregarPromocion():
    pass

def verPromocion():
    pass

def eliminarPromocion():
    pass

productos = []
encabezadosProd = ["id", "nombre", "precio", "stock"]
promociones = []
encabezadosProm = ["id", "precio"]

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
    print(" 7 - Salir del programa")

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
        eliminarPromocion()
    elif cadena == "7":
        salir = True