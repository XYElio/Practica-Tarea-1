#WHILE

# Pedir el valor de n al usuario
n = int(input("Introduce el valor de n: "))
suma = 0
i = 2
while n < 0:
    print("El número debe ser positivo. Inténtelo de nuevo.\n")
    n = int(input("Introduce el valor de n: "))



# Calcular la suma sigma utilizando un bucle for que incrementa en 2 unidades
while i <= 2 * n:
    suma += i
    i += 2

# Imprimir el resultado
print(f"La suma sigma de {n} es {suma}")
