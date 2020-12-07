from covid import Covid
covid = Covid(source = "worldometers")

control = False;
while control == False:
    # Solicitamos al usuario un nombre de un país
    cadena = input("Ingrese un nombre de un país: ")

    try:
        pais = covid.get_status_by_country_name(cadena) #obtener todos los datos del pais
        #print(pais) # Muestra todos los datos disponibles
        
        confirmados = pais.get("confirmed") # Se obtienen los casos confirmados
        fallecidos = pais.get("deaths") # Se obtienen los pacientes fallecidos
        recuperados = pais.get("recovered") # Se obtienen los pacientes recuperados
        activos = pais.get("active") # Se obtienen los casos activos
        criticos = pais.get("critical") # Se obtienen los casos activos críticos
        poblacion = pais.get("population") # Se obtiene la población total

        print("- Casos confirmados:", confirmados)
        print("- Casos activos:", activos)
        print("- Pacientes recuperados:", recuperados)
        print("- Pacientes fallecidos:", fallecidos)
        print("-------------------------------------------------")
        # Se controla que los datos coincidan (4to paso)
        if confirmados == (fallecidos + recuperados + activos):
            print("--Los datos concuerdan--")
        else:
            print("--Los datos no concuerdan--")
        # Se realizan diferentes cálculos solicitados (5to paso)
        print("-------------------------------------------------")
        
        totalMortalidad = ((fallecidos * 100) / confirmados)
        print("- Porcentaje de mortalidad:", "{0:.2f}".format(totalMortalidad), "%")
        totalRecuperados = ((recuperados * 100) / confirmados)
        print("- Porcentaje de recuperados:", "{0:.2f}".format(totalRecuperados), "%")
        totalCriticos = ((criticos * 100) / activos)
        print("- Porcentaje de casos críticos:", "{0:.2f}".format(totalCriticos), "%")
        totalPoblacion = ((confirmados * 100) / poblacion)
        print("- Porcentaje de casos según la población total:", "{0:.2f}".format(totalPoblacion), "%")

        # Mostrar tipo de mortalidad (7mo paso)
        print("-------------------------------------------------")
        if totalMortalidad < 2.00:
            print("- La mortalidad es baja")
        elif (totalMortalidad >= 2.00) and (totalMortalidad <= 3.50):
            print("- La mortalidad es media")
        elif totalMortalidad > 3.5:
            print("- La mortalidad es alta")

        control = True
    except:
        print("País no encontrado. Ingrese otro nombre, por favor.")

