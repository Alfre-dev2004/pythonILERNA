# Parte 1: Estructura inicial y crear alumnos
# Diccionario principal
alumnos = {}

# Añadimos 3 alumnos iniciales
alumnos["ana"] = {
    "edad": 19,
    "curso": "DAM2",
    "lenguajes": {"Python", "Java"},
    "nota": 7.5
}

alumnos["pablo"] = {
    "edad": 22,
    "curso": "DAW1",
    "lenguajes": {"JavaScript", "HTML", "CSS"},
    "nota": 4.5
}

alumnos["luis"] = {
    "edad": 17,
    "curso": "ASIR1",
    "lenguajes": {"Bash", "Python"},
    "nota": 9.2
}

# Parte 5: Bucle while con menú
while True:
    print("\n--- MENÚ ALUMNOS ---")
    print("1. Mostrar alumnos")
    print("2. Buscar alumno")
    print("3. Añadir alumno")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Parte 2: Mostrar alumnos y Parte 3: Condicionales sobre notas
        print("\n--- LISTA DE ALUMNOS ---")
        suma_notas = 0
        total_alumnos = 0
        
        # Recorremos el diccionario
        for nombre, datos in alumnos.items():
            print(f"Alumno: {nombre.capitalize()}")
            print(f"Edad: {datos['edad']}")
            print(f"Curso: {datos['curso']}")
            # Convertimos el set a string para mostrarlo limpio
            print(f"Lenguajes: {', '.join(datos['lenguajes'])}")
            
            nota = datos['nota']
            calificacion = ""
            
            # Condicionales de nota
            if nota < 5:
                calificacion = "Suspenso"
            elif nota >= 5 and nota < 7:
                calificacion = "Aprobado"
            elif nota >= 7 and nota < 9:
                calificacion = "Notable"
            elif nota >= 9:
                calificacion = "Sobresaliente"
                
            print(f"Nota media: {nota} ({calificacion})")
            print("-" * 20)
            
            # Para el reto final
            suma_notas += nota
            total_alumnos += 1

        # Parte 4: Filtrar alumnos (Mayores de 18 y nota >= 7)
        print("\n--- ALUMNOS DESTACADOS (>18 y Nota >= 7) ---")
        for nombre, datos in alumnos.items():
            if datos["edad"] > 18 and datos["nota"] >= 7:
                print(f"- {nombre.capitalize()} cumple los requisitos.")

        # Reto final: Media de notas
        if total_alumnos > 0:
            media_total = suma_notas / total_alumnos
            print(f"\nLa media global de la clase es: {media_total:.2f}")

    elif opcion == "2":
        # Parte 6: Buscar alumno
        busqueda = input("Dime el nombre del alumno: ").lower()
        
        if busqueda in alumnos:
            datos = alumnos[busqueda]
            print(f"\nEncontrado: {busqueda.capitalize()}")
            print(f"Edad: {datos['edad']}")
            print(f"Curso: {datos['curso']}")
            print(f"Lenguajes: {datos['lenguajes']}")
            print(f"Nota: {datos['nota']}")
        else:
            print("Alumno no encontrado.")

    elif opcion == "3":
        # Parte 7: Añadir alumno
        print("\n--- AÑADIR ALUMNO ---")
        nombre_nuevo = input("Nombre (o escribe 'salir' para cancelar): ").lower()
        
        # Parte 8: Uso de break
        if nombre_nuevo == "salir":
            print("Cancelando...")
            # Volvemos al inicio del while sin guardar nada
            continue
            
        # Pedimos el resto de datos
        try:
            edad_nueva = int(input("Edad: "))
            curso_nuevo = input("Curso: ")
            # Convertimos lenguajes a set separando por comas
            lenguajes_str = input("Lenguajes (separados por coma): ")
            lenguajes_set = set(lenguajes_str.split(","))
            nota_nueva = float(input("Nota media: "))
            
            # Guardamos en el diccionario
            alumnos[nombre_nuevo] = {
                "edad": edad_nueva,
                "curso": curso_nuevo,
                "lenguajes": lenguajes_set,
                "nota": nota_nueva
            }
            print("Alumno guardado correctamente.")
            
        except ValueError:
            print("Error: La edad o la nota deben ser números.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción incorrecta, prueba otra vez.")