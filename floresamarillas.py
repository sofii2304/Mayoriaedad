import time
import random

# Función para imprimir un huevo
def print_egg():
    egg = """
         ,ggg,
       ,g@@@@@@g,
     ,g@@@@@@@@@@g,
   ,@@@@@@@@@@@@@@@g,
  @@@@@@@@@@@@@@@@@@g
 @@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@    _
@@@@@@@@@@@@@@@@@@@@  .(_)
@@@@@@@@@@@@@@@@@@   /   \
@@@@@@@@@@@@@@@@@   |     |
@@@@@@@@@@@@@@@@'   \    |
@@@@@@@@@@@@@@@'     |   /
@@@@@@@@@@@@@@'       |._|
@@@@@@@@@@@@@'

"""
    print(egg)

# Función para imprimir la gallina
def print_chicken():
    chicken = """
   _
   \( )
    | |
  \ | |
  / | |
 / / | |
 | | | |
 | | | |
 / | | \
 | | | |
/  | |  \
| / | \  \
||| | ||| |
| | | | | |
 \ | | | |
   | | | |
  / | | \ \
 | | | | | |
 | | | | | |
 | | | | | |
   | | | |
   / | | \
   | | | |
   \ | | /
     | |
    |   |
    |   |
    |   |
    |   |
    |___|

"""
    print(chicken)

# Función principal
def main():
    print("¡La gallina está poniendo huevos!\n")

    for _ in range(6):  # Poner al menos 6 huevos
        time.sleep(1)  # Esperar 1 segundo antes de poner el huevo
        print_chicken()
        time.sleep(1)  # Esperar 1 segundo antes de imprimir el huevo
        print_egg()
        print("\n")

if __name__ == "__main__":
    main()
