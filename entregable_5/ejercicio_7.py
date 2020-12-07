# 2 equipos de 6 personas
# 1 es el jefe, mientras que los restantes 5 son oficiales

alfabeto = "abcdefghijklmnopqrstuvwxyz"

cadena = input("Ingrese el valor de corrimiento a utilizar: ")
corrimiento = int(cadena)

for i in range(5):
    cadena = input("Ingrese el mensaje a encriptar: ")
    encriptado = ""
    for caracter in cadena:
        if caracter.lower() in alfabeto:
            indice = alfabeto.find(caracter.lower())
            indice = (indice+corrimiento)%27
            encriptado += alfabeto[indice]
        else:
            encriptado += caracter

    print("El mensaje encriptado es: ", encriptado)