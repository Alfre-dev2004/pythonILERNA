# ============================================
# REPASO PYTHON PARA EXAMEN – LO ESENCIAL
# ============================================

# ------------------------------
# 1. TIPOS DE DATOS
# ------------------------------

# String
mensaje = "Hola Python"
print(mensaje)

# Entero, decimal, complejo
entero = 10
decimal = 3.14
complejo = 2 + 5j
print(entero, decimal, complejo)

# Booleano
activo = True
print(activo)

# type() → ver tipo de dato
print(type(mensaje))
print(type(entero))
print(type(decimal))
print(type(activo))


# ------------------------------
# 2. VARIABLES Y CONVERSIÓN DE TIPOS
# ------------------------------

nombre = "Geral"
edad = 35
print(nombre, edad)

# Convertir entero a string
edad_str = str(edad)
print(edad_str, type(edad_str))

# len() → contar caracteres
print(len("Python"))


# ------------------------------
# 3. INPUT (comentado para evitar detener el programa)
# ------------------------------

"""
nombre_usuario = input("¿Cómo te llamas? ")
print("Hola", nombre_usuario)
"""


# ------------------------------
# 4. OPERADORES
# ------------------------------

# Aritméticos
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)   # división entera
print(10 % 3)    # resto
print(2 ** 3)    # potencia

# Concatenar strings
print("Hola" + " Python")

# Repetir strings
print("Hola " * 3)

# Comparaciones
print(3 > 4)
print(3 < 4)

# Comparar strings por ASCII
print("Hola" < "Python")  # True (H = 72, P = 80)

# Operadores lógicos
print(3 < 4 and 5 > 2)   # True
print(3 < 4 or 5 < 2)    # True
print(not(3 < 4))        # False

# Prioridad lógica: () → not → and → or
print(3 < 4 or (5 > 10 and 2 == 2))


# ------------------------------
# 5. STRINGS (cadenas)
# ------------------------------

texto = "Python"

# Concatenación
print("Hola " + texto)

# Caracteres especiales
print("Linea 1\nLinea 2")
print("\tTabulado")

# Slicing
print(texto[1:3])   # yt
print(texto[:3])    # Pyt
print(texto[-2:])   # on

# Invertir string
print(texto[::-1])

# Métodos importantes de strings
lenguaje = "python"

print(lenguaje.capitalize())     # Python
print(lenguaje.upper())          # PYTHON
print(lenguaje.count("t"))       # 1
print(lenguaje.isnumeric())      # False
print("123".isnumeric())         # True
print(lenguaje.lower())          # python
print(lenguaje.upper().isupper())  # True
print(lenguaje.startswith("py"))   # True


# ------------------------------
# 6. LISTAS
# ------------------------------

# Crear lista
lista = [35, 24, 62]
print(lista)

# Acceder elementos
print(lista[0])
print(lista[-1])

# Modificar lista
lista[1] = 50
print(lista)

# Métodos de listas
lista.append(100)        # agregar al final
lista.insert(1, "Hola")  # insertar
lista.remove(62)         # eliminar por valor
print(lista)

# pop() elimina por índice
lista.pop(0)
print(lista)

# copy() → copiar lista
copia = lista.copy()
print(copia)

# clear() → vaciar lista
copia.clear()
print(copia)

# Concatenar listas
print([1, 2] + [3, 4])


# ------------------------------
# 7. TUPLAS
# ------------------------------

tupla = (35, 1.60, "Geral")
print(tupla)

# Acceder
print(tupla[0])
print(tupla[-1])

# Convertir tupla → lista → modificar → volver a tupla
lista_temp = list(tupla)
lista_temp[0] = 99
tupla = tuple(lista_temp)
print(tupla)


# ------------------------------
# 8. SETS (conjuntos)
# ------------------------------

# Crear set (no tiene orden)
s = {"Geral", "Lopez", 35}
print(s)

# Añadir elemento (no permite duplicados)
s.add("Python")
s.add("Geral")  # no se duplica
print(s)

# Los sets no tienen índices
# s[0] → ERROR


# ------------------------------
# FIN DEL REPASO
# ------------------------------
