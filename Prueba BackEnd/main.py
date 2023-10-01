from Tecnologia import Tecnologia
from Bicicletas import Bicicletas
from Tvs import Tvs
from Bicicletas import Bicicletas
from Consolas import Consolas
from Scooters import Scooters

def menu():

    listaTvs = []
    listaConsolas = []
    listaScooters= []
    listaBicicletas= []
    productos = listaBicicletas + listaConsolas + listaScooters + listaBicicletas
    total = 0

    while True:
        print("\nMenú:")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar")
        print("6. Ver informacion")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Marca del TV: ")
            voltaje = input("Voltaje: ")
            eficiencia = input("Nivel de eficiencia (A, B, C, D, E, F): ").upper()
            precio = float(input("Precio del TV: "))
            tamaño = input("Tamaño del TV (pulgadas): ")

            tv = Tvs(marca, voltaje, eficiencia, precio, tamaño)
            listaTvs.append(tv)
            print("TV registrado con éxito.")

        elif opcion == "2":
            marca = input("Marca de la consola: ")
            voltaje = input("Voltaje: ")
            eficiencia = input("Nivel de eficiencia (A, B, C, D, E, F): ").upper()
            precio = float(input("Precio de la consola: "))
            nombre = input("Nombre de la consola: ")
            version = input("Versión de la consola: ")
            lite = input("¿Es versión Lite? (Sí/No): ").lower() == "sí"

            consola = Consolas(marca, voltaje, eficiencia, precio, nombre, version, lite)
            listaConsolas.append(consola)
            print("Consola registrada con éxito.")

        elif opcion == "3":
            marca = input("Marca del scooter: ")
            voltaje = input("Voltaje: ")
            eficiencia = input("Nivel de eficiencia (A, B, C, D, E, F): ").upper()
            precio = float(input("Precio del scooter: "))
            aro = int(input("Aro del scooter: "))
            velocidad = int(input("Velocidad del scooter (km/h): "))
            peso = float(input("Peso del scooter (kg): "))

            scooter = Scooters(marca, voltaje, eficiencia, precio, aro, velocidad, peso)
            listaScooters.append(scooter)
            print("Scooter registrado con éxito.")

        elif opcion == "4":
            aro = int(input("Ingrese el aro de la Bicicleta: "))
            peso = float(input("Ingrese el peso de la Bicicleta kg: "))
            precio = float(input("Ingrese el precio de la Bicicleta: "))
            marca = input("Ingrese la marca de la Bicicleta: ")

            bicicleta = Bicicletas(aro, precio, peso, marca)
            listaBicicletas.append(bicicleta)
            print("Bicicleta registrada.")

        elif opcion == "5":
            if 'tv' in locals() and isinstance(tv, Tvs):
                print("\nCotización de TV:")
                print(tv.cotizar())
            if 'consola' in locals() and isinstance(consola, Consolas):
                print("\nCotización de Consola:")
                print(consola.cotizar())
            if 'scooter' in locals() and isinstance(scooter, Scooters):
                print("\nCotización de Scooter:")
                print(scooter.cotizar())

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()