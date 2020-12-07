cadena = input("Ingrese una frase: ")

cantidad = 0
for x in cadena:
    if x in "aeiou":
        cantidad += 1

print("Cantidad de vocales encontradas: ", cantidad)