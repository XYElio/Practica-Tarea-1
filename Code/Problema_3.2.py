#FOR

producto = 1
# Pedir el valor de n al usuario
n = int(input("Introduce el valor de n: "))
while n < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.\n")
    n = int(input("Introduce el valor de n: "))

# Calcular el producto de la secuencia
for i in range(2, 2 * n + 1, 2):
    producto *= i

# Imprimir el resultado
print(f"El producto de la secuencia de 1 hasta {n} es {producto}")