cadena = input("Ingrese una frase: ")

cantidad = 0
vocalesUsadas = ""
for x in cadena:
    if x in "aeiou":
        if x not in vocalesUsadas:
            cantidad += 1
            vocalesUsadas += x 

print("Cantidad de vocales encontradas: ", cantidad)
print("Vocales usadas: ", vocalesUsadas)