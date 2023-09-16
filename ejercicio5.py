# Solicita al usuario que ingrese una lista de palabras separadas por espacios
palabras = input("Por favor, ingresa una lista de palabras separadas por espacios: ")

# Convierte la entrada en una lista de palabras
lista_palabras = palabras.split()

# Solicita al usuario que ingrese la letra con la que deseas filtrar las palabras
letra_inicial = input("Por favor, ingresa la letra inicial para filtrar las palabras: ")

# Utiliza un ciclo for y una estructura condicional if para mostrar las palabras que empiezan con la letra determinada
print(f"Palabras que empiezan con '{letra_inicial}':")
for palabra in lista_palabras:
    if palabra.startswith(letra_inicial):
        print(palabra)