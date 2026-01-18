# Calculadora
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b
# Menú de opciones
print("Seleccione operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
# Entrada del usuario
opcion = input("Ingrese opción (1/2/3/4): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Ejecutar operación
if opcion == '1':
    print(f"Resultado: {sumar(num1, num2)}")
elif opcion == '2':
    print(f"Resultado: {restar(num1, num2)}")
elif opcion == '3':
    print(f"Resultado: {multiplicar(num1, num2)}")
elif opcion == '4':
    print(f"Resultado: {dividir(num1, num2)}")
else:
    print("Opción inválida")