import os
from director.bus import BusDirector
from director.walk import WalkDirector
from director.car import CarDirector


def routeCalculation(data):  # Call the director methods and expose them in different cases
    WALK = WalkDirector.construct(data['origin'], data['destiny'])
    CAR = CarDirector.construct(data['origin'], data['destiny'])
    BUS = BusDirector.construct(data['origin'], data['destiny'])
    if data['option'] == 1:
        print(WALK.construction())
    elif data['option'] == 2:
        print(CAR.construction())
    elif data['option'] == 3:
        print(BUS.construction())
    elif data['option'] == 4:
        print(WALK.construction())
        print(CAR.construction())
        print(BUS.construction())
    return True


def cleanScreen():  # Clean the console for OS unix and windows
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def menu():  # Menu to operate with commands
    cleanScreen()
    while True:
        print(
            """
    ASISTENTE DE RUTAS

    1) Trazar ruta.
    0) salir

            """
        )
        option = int(input("Seleccione una opción: "))
        if option == 0:
            cleanScreen()
            exit()
        elif 0 != option != 1:
            cleanScreen()
            continue
        elif option == 1:
            cleanScreen()
            print("""TRAZAR RUTA""")
            origin = input("Ingrese la ubicación de partida: ")
            destiny = input("Ingrese la ubicación de destino: ")
            print(
                """
    MÉTODOS DE TRANSPORTE DISPONIBLES

    1) Caminando
    2) Carro
    3) Bus
    4) Comparar todas

    0) Salir

            """
            )
            option = int(input("Seleccione una opción: "))
            if option == 1 or option == 2 or option == 3 or option == 4:
                cleanScreen()
                data = {
                    'option': option,
                    'origin': origin,
                    'destiny': destiny
                }
                routeCalculation(data)
                input("")
            elif option == 0:
                cleanScreen()
                exit()
            elif 0 != option != 1:
                cleanScreen()
                continue


menu()  # Execute script
