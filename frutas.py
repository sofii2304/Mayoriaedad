# Crea una lista de 5 nombres de frutas
frutas = ["manzana", "banana", "naranja", "fresa", "kiwi"]

# Utiliza un ciclo for para imprimir cada nombre de la lista
print("Nombres de frutas:")
for fruta in frutas:
    print(fruta)

# Utiliza otro ciclo for para imprimir cada letra de cada nombre de la lista
print("\nLetras de los nombres de frutas:")
for fruta in frutas:
    for letra in fruta:
        print(letra)