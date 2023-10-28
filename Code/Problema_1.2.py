#FOR

suma = 0
# Pedir el valor de n al usuario
n = int(input("Introduce el valor de n: "))

while n < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.\n")
    n = int(input("Introduce el valor de n: "))


# Calcular la suma sigma utilizando un bucle for que incrementa en 2 unidades
for i in range(2, 2 * n + 1, 2):
    suma += i

# Imprimir el resultado
print(f"La suma sigma de {n} es {suma}")
