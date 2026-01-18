
# -----------------------------------------------------------
# LISTAS PRINCIPALES (datos inventados)
# -----------------------------------------------------------

alumnos = ["Nahuel", "Alfredo", "Sara", "Sara", "Xavi",
           "Nahuel", "Bianca", "Jonathan", "Biel", "Bianca"]

edades = [19, 22, 20, 23, 18, 25, 19, 21, 24, 20]

cursos = ["DAM1", "DAM2", "DAW1", "DAW2", "DAM1",
          "DAM2", "DAW2", "DAM2", "DAW1", "DAM1"]

modulos = ["Programación", "BBDD", "Sistemas", "Redes", "FOL", "Seguridad"]
profes = ["Jordi", "Cristina", "Miguel", "Laura", "Sonia", "Pablo"]

matriculas = ["MAT01", "MAT02", "MAT03", "MAT04",
              "MAT01", "MAT05", "MAT06", "MAT07"]

# -----------------------------------------------------------
# A. ALTAS, BAJAS Y CAMBIOS
# -----------------------------------------------------------

def alta_alumno():
    print("\n--- Alta de alumno/a ---")
    nombre = input("Nombre: ")
    try:
        edad = int(input("Edad: "))
    except:
        print("Edad inválida.")
        return
    curso = input("Curso (DAM1/DAM2/DAW1/DAW2): ")

    # Usamos append porque es lo que pide la actividad
    alumnos.append(nombre)
    edades.append(edad)
    cursos.append(curso)

    print(f"Alumno/a '{nombre}' añadido correctamente.")


def baja_alumno():
    print("\n--- Baja de alumno/a ---")
    nombre = input("Nombre a eliminar: ")

    if nombre not in alumnos:
        print("No existe ese nombre.")
        return

    # Eliminamos solo la primera coincidencia
    idx = alumnos.index(nombre)

    alumnos.remove(nombre)       # borra por nombre
    edades.pop(idx)              # borra por índice para mantener paralelismo
    cursos.pop(idx)

    print(f"El alumno/a '{nombre}' ha sido eliminado.")


def cambiar_curso():
    print("\n--- Cambio de curso ---")
    nombre = input("Nombre del alumno/a: ")

    if nombre not in alumnos:
        print("Ese alumno/a no existe.")
        return

    nuevo = input("Nuevo curso: ")
    idx = alumnos.index(nombre)
    cursos[idx] = nuevo

    print(f"Curso actualizado para {nombre} → {nuevo}")

# -----------------------------------------------------------
# B. CONSULTAS Y LISTADOS
# -----------------------------------------------------------

def listar_por_curso():
    print("\n--- Listado por curso ---")
    curso = input("Curso a buscar: ")

    print(f"\nAlumnos en {curso}:")
    encontrado = False
    for i in range(len(alumnos)):
        if cursos[i] == curso:
            print(f"- {alumnos[i]} ({edades[i]} años)")
            encontrado = True

    if not encontrado:
        print("No hay alumnos en ese curso.")


def top_edades():
    print("\n--- Top edades ---")
    copia = edades.copy()
    copia.sort()

    print(f"Menor edad: {copia[0]}")
    print(f"Mayor edad: {copia[-1]}")


def contar_repetidos():
    print("\n--- Conteo de repetidos ---")
    nombre = input("Nombre a contar: ")
    rep = alumnos.count(nombre)

    print(f"'{nombre}' aparece {rep} veces.")


def buscar_modulo():
    print("\n--- Búsqueda de módulo ---")
    nombre = input("Nombre del módulo: ")

    if nombre not in modulos:
        print("Ese módulo no existe.")
        return

    idx = modulos.index(nombre)
    print(f"Módulo encontrado en posición {idx}")
    print(f"Profesor/a: {profes[idx]}")

# -----------------------------------------------------------
# C. OPERACIONES CON LISTAS
# -----------------------------------------------------------

def union_grupos():
    print("\n--- Unión de grupos ---")
    alumnos_DAM = ["Pedro", "María"]
    alumnos_DAW = ["Lucía", "Carlos"]

    alumnos_totales = alumnos_DAM + alumnos_DAW

    print("Grupo unificado:", alumnos_totales)


def reverso_y_slicing():
    print("\n--- Reverso y primeros 5 ---")

    print("Alumnos al revés:")
    print(alumnos[::-1])

    print("\nPrimeros 5 alumnos:")
    print(alumnos[:5])


def limpieza_controlada():
    print("\n--- Limpieza controlada de matrícula ---")

    copia = matriculas.copy()
    copia.clear()     # limpiar solo la copia

    print("Original:", matriculas)
    print("Copia vaciada:", copia)

# -----------------------------------------------------------
# D. MINI-REPORTES
# -----------------------------------------------------------

def resumen_iilerna():
    print("\n--- Resumen IILERNA ---")

    print("Total alumnos:", len(alumnos))
    print("Total módulos:", len(modulos))
    print("Total matrículas:", len(matriculas))

    print("\nAlumnos por curso:")
    for c in ["DAM1", "DAM2", "DAW1", "DAW2"]:
        print(f"{c}: {cursos.count(c)}")


def profes_y_modulos():
    print("\n--- Profes → Módulos ---")
    for i in range(len(modulos)):
        print(f"{profes[i]} → {modulos[i]}")


def edades_por_tramo():
    print("\n--- Edades por tramo ---")

    m20 = 0
    entre = 0
    g25 = 0

    for e in edades:
        if e < 20:
            m20 += 1
        elif 20 <= e <= 24:
            entre += 1
        else:
            g25 += 1

    print(f"Menores de 20: {m20}")
    print(f"Entre 20 y 24: {entre}")
    print(f"25 o más: {g25}")


def normalizar_nombres():
    print("\n--- Normalizador de nombres ---")

    for i in range(len(alumnos)):
        alumnos[i] = alumnos[i].capitalize()

    print("Nombres normalizados.")


def depurar_duplicados():
    print("\n--- Eliminación de duplicados ---")

    sin_repetidos = []
    for nombre in alumnos:
        if nombre not in sin_repetidos:
            sin_repetidos.append(nombre)

    print("Lista sin repetidos:", sin_repetidos)
    
    




# -----------------------------------------------------------
# MENÚ PRINCIPAL
# -----------------------------------------------------------

def menu():
    while True:
        print("\n========= MENÚ IILERNA =========")
        print("1. Alta alumno")
        print("2. Baja alumno")
        print("3. Cambio de curso")
        print("4. Listar por curso")
        print("5. Top edades")
        print("6. Contar nombre repetido")
        print("7. Buscar módulo")
        print("8. Unión de grupos")
        print("9. Reverso y slicing")
        print("10. Limpieza controlada")
        print("11. Resumen IILERNA")
        print("12. Profes y módulos")
        print("13. Edades por tramo")
        print("14. Normalizar nombres")
        print("15. Quitar duplicados")
        print("0. Salir")

        op = input("Elige una opción: ")

        if op == "1": alta_alumno()
        elif op == "2": baja_alumno()
        elif op == "3": cambiar_curso()
        elif op == "4": listar_por_curso()
        elif op == "5": top_edades()
        elif op == "6": contar_repetidos()
        elif op == "7": buscar_modulo()
        elif op == "8": union_grupos()
        elif op == "9": reverso_y_slicing()
        elif op == "10": limpieza_controlada()
        elif op == "11": resumen_iilerna()
        elif op == "12": profes_y_modulos()
        elif op == "13": edades_por_tramo()
        elif op == "14": normalizar_nombres()
        elif op == "15": depurar_duplicados()
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")



# Ejecutar menú
menu()