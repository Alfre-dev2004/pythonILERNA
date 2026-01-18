#Alfredo Noriega Aranda

frase = input("Dame una frase: ")
cont_a=frase.count("a")
print("El numero de a en la frase son : ", cont_a)

palabra = input("Dame una palabra : ")
palabra_mayus = palabra.upper() #La cambio a mayuscula
palabra_minus = palabra.lower()#La cambi a minuscula
palabra_cap = palabra.capitalize() #La primera letra a mayuscula
 
print("Tu palabra en mayusculas es: ", palabra_mayus)
print("Tu palabra en minusculas es: ", palabra_minus)
print("Tu palabra capitalizada es: ", palabra_cap)