print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Hola")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

print(not "Hola" or "Python")

print("" or "Hola" and "Python")

print("" or "Hola" and "Python")

print(not ("Hola" or "") and "Python")

print("A" < "B" and not ("Z" > "a"))

"""
1. Escribe en Python cinco ejemplos diferentes usando el operador not.
2. En cada caso, combina not con comparaciones numéricas, de texto o valores
booleanos.
3. Antes de ejecutar el programa, predice si el resultado será True o False.
4. Ejecuta tu código y verifica si tu predicción fue correcta.
5. Agrega un comentario al lado de cada línea explicando por qué el resultado es
así.

"""
print(not (5 < 3))   #  True → ya que 5 < 3 es falso, y "not" invierte el valor

print(not (10 > 2))  #  False → el "not" invierte el resultado verdadero

print(not ("hola" == "adiós"))  #  True → las cadenas son diferentes, y el not invierte el falso

print(not True)  #  False → el not cambia True a False


print(not (3 > 7 or 2 == 2))  # False → porque (3 > 7 or 2 == 2) da True, y not lo invierte