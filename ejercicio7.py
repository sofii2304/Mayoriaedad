# Define el número para el cual deseas generar la tabla de multiplicar
numero = 6

# Utiliza un ciclo for para generar la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")