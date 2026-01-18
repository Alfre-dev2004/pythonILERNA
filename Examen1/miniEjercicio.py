#Alfredo Noriega Aranda

nombre = input("Dame tu nombre: ") #Le pido el nombre
edad = input("Dame tu edad: ")#Le pido edad
ciudad = input("Dame tu ciudad: ")#Le pido ciudad

edad = int(edad)#Convierto a int

datos_usuario = [nombre,edad,ciudad] #Los guardo en la lista

print(datos_usuario)

print(f"Me llamo {nombre}, tengo {edad} y vivo en {ciudad}")
print("Los elementos de la lista es: ",len(datos_usuario))