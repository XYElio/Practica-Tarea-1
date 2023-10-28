#WHILE

i = 1 
producto = 1
# Pedir el valor de n al usuario
n = int(input("Introduce el valor de n: "))
while n < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.\n")
    n = int(input("Introduce el valor de n: "))


# Calcular el producto de la secuencia
while i <= n:
    producto *= i
    i += 1

# Imprimir el resultado
print(f"El producto de la secuencia de 1 hasta {n} es {producto}")
