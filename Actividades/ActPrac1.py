#Parte 1
print("---------------------------Datos personales---------------------------")
name= "Alfredo Isaias Noriega Aranda"
edad = 20
student = True

print("Mi nombre es ",name," tengo ",edad," años ") 
print("Estado de estudiante: ",student)
print("name: ",type(name),"\nEdad: ",type(edad),"\nStudent: ",type(student))
edad = 21 #Cambio de variable
print("En mi cumpleaños cumpliré ",edad," años ")

#Parte 2
print("---------------------------Gustos personales---------------------------")

elementos = []#Creamos la lista vacia 

for i in range(3): #Iniciamos el bucle con maximo de 3
    gustos = input(f"Dime 3 cosas que te gusten: ") #Pedimos al usuario
    elementos.append(gustos)#Guardamos en la lista
    
    

print(elementos)
print("Cuantos elementos hay: ", len(elementos))#Muestra cuantos elementos hay en la lista
gustos_modificados = elementos * 2
print(gustos_modificados)#Lo que hace es duplicar el contenido de la lista

#Parte 3
print("---------------------------Comidas favoritas---------------------------")
comidas_favoritas = ("arroz_con_pollo","tallarines_rojos","milanesa")
print(comidas_favoritas)
# comidas_favoritas[2] = "estofado" ---------->Da error porque las tuplas son inmutables osea no se puede cambiar
print(len(comidas_favoritas))

#Parte 4
print("---------------------------Conjunto de numeros---------------------------")
numeros = {1, 2, 2, 3, 4, 4, 5}#Los valores duplicados se eliminan y solo sale uno
print(numeros)
numeros = numeros | {6}
print(numeros)  #El numero no se repite porque es un set

#Parte 5
print("---------------------------Tipos de datos y resumen---------------------------")
print(type(name))
print(type(elementos))
print(type(comidas_favoritas))
print(type(numeros))
resumen = [gustos, comidas_favoritas, numeros]
print(resumen) #Se combinan todas las listan en una sola

#Parte 6
print("---------------------------Reto de logica---------------------------")

if edad < 18: #Si edad es menor a 18 es menor
    print("Eres menor de edad")
elif edad >= 18 and edad <= 30 : #Si edad esta entre 18 y 30 es joven
    print("Eres joven")
else: #Sino es un adulto
    "Eres adulto"
    
