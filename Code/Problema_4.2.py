#FOR

suma = 0
# Pedir el valor de n al usuario
n = int(input("Introduce el valor de n: "))
while n < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.\n")
    n = int(input("Introduce el valor de n: "))


for i in range(1, n + 1):
    suma += i ** 3

# Imprimir el resultado
print(f"La suma de las potencias cúbicas de 1 hasta {n} es {suma}")
