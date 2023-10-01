from Tecnologia import Tecnologia
from Bicicletas import Bicicletas
from Tvs import Tvs
from Bicicletas import Bicicletas
from Consolas import Consolas
from Scooters import Scooters
from Transporte import Transporte

def menu():

    listaTvs = []
    listaConsolas = []
    listaScooters= []
    listaBicicletas= []
    total = 0

    print("- B I E N V E N I D O -")

    while True:
        print("\nMenú:")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar")
        print("6. Salir.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Marca del TV: ")
            voltaje = input("Voltaje: ")
            eficiencia = input("Nivel de eficiencia (A, B, C, D, E, F): ").upper()
            precio = float(input("Precio del TV: "))
            tamaño = input("Tamaño del TV (pulgadas): ")

            tv = Tvs(marca, voltaje, eficiencia, precio, tamaño)
            listaTvs.append(tv)
            tv.__str__()

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
            consola.__str__()

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
            scooter.__str__()

        elif opcion == "4":
            aro = int(input("Ingrese el aro de la Bicicleta: "))
            peso = float(input("Ingrese el peso de la Bicicleta kg: "))
            precio = float(input("Ingrese el precio de la Bicicleta: "))
            marca = input("Ingrese la marca de la Bicicleta: ")

            bicicleta = Bicicletas(aro, precio, peso, marca, 4000)
            listaBicicletas.append(bicicleta)
            costo_despacho = bicicleta.calcular_costo_despacho()
            print(f"Costo de despacho de la bicicleta: ${costo_despacho}")
            bicicleta.__str__()

        elif opcion == "5":
            for tv in listaTvs:
                print("\nCotización de TV:")
                print(tv.cotizar())

            for consola in listaConsolas:
                print("\nCotización de Consola:")
                print(consola.cotizar())

            for scooter in listaScooters:
                print("\nCotización de Scooter:")
                print(scooter.cotizar())

            for bicicleta in listaBicicletas:
                print("\nCotización de Bicicleta:")
                print(bicicleta.cotizar())
            
            if not listaTvs and not listaConsolas and not listaScooters and not listaBicicletas:
                print("No se encontró ningún producto registrado.")

        elif opcion == "6":
            print("Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida!")


if __name__ == "__main__":
    menu()