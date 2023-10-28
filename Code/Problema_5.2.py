#FOR


num1 = int(input("Ingrese el primer número entero positivo: "))
while num1 < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.")
    num1 = int(input("Ingrese el primer número entero positivo: "))

num2 = int(input("Ingrese el segundo número entero positivo: "))
while num2 < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.")
    num2 = int(input("Ingrese el segundo número entero positivo: "))

resultado = 0
for i in range(num2):
    resultado += num1

print(f"El producto de {num1} y {num2} es {resultado}")
