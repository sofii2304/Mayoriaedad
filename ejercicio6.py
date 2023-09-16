# Solicita al usuario que ingrese la primera lista de números separados por espacios
input1 = input("Por favor, ingresa la primera lista de números separados por espacios: ")

# Solicita al usuario que ingrese la segunda lista de números separados por espacios
input2 = input("Por favor, ingresa la segunda lista de números separados por espacios: ")

# Convierte las entradas en listas de números
lista1 = [int(x) for x in input1.split()]
lista2 = [int(x) for x in input2.split()]

# Verifica si ambas listas tienen la misma longitud
if len(lista1) != len(lista2):
    print("Las listas deben tener la misma longitud para realizar la suma.")
else:
    # Inicializa una lista vacía para almacenar la suma de los elementos
    suma_lista = []

    # Utiliza un ciclo for para calcular la suma de los elementos en la misma posición
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        suma_lista.append(suma)

    # Muestra la lista resultante
    print("La lista resultante de la suma de elementos es:", suma_lista)