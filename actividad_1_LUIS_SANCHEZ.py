"""
---
title: 04GIAR Fundamentos de la programación.
subtitle: ACTIVIDAD 1: INTRODUCCIÓN A PYTHON
author: 2024@Luis, Sánchez.

Definición del jugador
- Función Introducir un nuevo jugador
-- debe validar que el dorsal no está repetido
-- la función debe recibir nombre, dorsal, canastas_3, canastas_2, canastas_1
-- debo guardar los jugadores en una lista
-- al guardar los valores sumar las canastas y guardar el total
-- la lista debe tener todos los datos de los jugadores.

- Función Listar los jugadores 
-- obtener toda la lista
-- obtener la lista por jugador
-- en este listado las anotaciones deben ser totales por jugador

- Función Máximo Anotador
-- Sumar los totales de las canastas de 3, 2 y 1 de cada jugador, devolver el jugador con el número mayor

- Función Estadísticas del equipo
-- Listar todos los jugadores con los valores de cada canasta y el total 

- Función Salir del Programa
"""

players = []


def is_number(number):
    # predicado para verificar que el valor es númerico
    return number.isdigit()


def sum_all_scores(canastas_1, canastas_2, canastas_3):
    """
    Función que suma todos los puntajes y devuelve un total
    :param canastas_1: int
    :param canastas_2: int
    :param canastas_3: int
    :return: sum of each of the scores
    """
    result = canastas_1 + canastas_2 + canastas_3
    return result


def create_nuevo_jugador(nombre, dorsal, canastas_1, canastas_2, canastas_3):
    """
    Función que crea el nuevo jugador a portir de un set de parámetros
    No se considera que llegue un valor vacío porque siempre se válida que tenga un input
    :param nombre: String
    :param dorsal: Int
    :param canastas_1: Int
    :param canastas_2: Int
    :param canastas_3: Int
    :return: Devuelve True luego de crearlo
    """
    # Suma los puntajes y lo agrega a la lista como total
    total = sum_all_scores(canastas_1, canastas_2, canastas_3)
    # Agrega los valores a la lista
    players.append([nombre, dorsal, canastas_1, canastas_2, canastas_3, total])
    return True


def get_jugadores(estadistica_or_lista):
    """
    Función para listar la estadistica o la lista de jugadores, itera sobre la lista de acuerdo al parametro
    :param estadistica_or_lista: recibe "estadistica" o "lista"
    :return: cadena de texto con los valores de la lista seleccionada
    """
    result = ""
    # Si no hay jugadores en la lista le pide que cree uno
    if len(players) == 0:
        result = "\nNo hay jugadores, crea un jugador con la opción[1]\n"
    for index, player in enumerate(players):
        if estadistica_or_lista == "lista":
            result += (f'Jugador {index + 1}: Nombre {player[0]} | '
                       f'Dorsal: {player[1]} | '
                       f'Total anotaciones: {player[-1]}.\n')
        else:
            result += (f'Jugador {index + 1}: Nombre {player[0]} | '
                       f'Dorsal: {player[1]} | '
                       f'Canasta 1: {player[2]} | '
                       f'Canasta 2: {player[3]} | '
                       f'Canasta 3: {player[4]} | '
                       f'Total anotaciones: {player[-1]}.\n')
    return result


def get_max_anotador():
    """
    Función que haya el resultado máximo entre los jugadores agregados a la lista
    El metodo max: recibe una lista a iterar y utiliza la función lambda. Compara usando el segundo elemento de cada sublista
    # Hace internamente esto (ejemplo tomado de ChatGPT porque no conocía el método)
    # jugadores = [["Juan", 10, 40], ["Ana", 15, 45], ["Pedro", 12, 42]]
    # 1. Para ["Juan", 10, 40] → devuelve 40
    # 2. Para ["Ana", 15, 45] → devuelve 45
    # 3. Para ["Pedro", 12, 42] → devuelve 42
    # 4. Compara: 40 vs 45 vs 42
    # 5. Identifica que 45 es el mayor
    # 6. Devuelve la lista completa ["Ana", 15, 45]
    :return: String con el jugador y el número de anotaciones total
    """
    result = ""
    if len(players) > 0:
        result = max(players, key=lambda x: x[-1])
        result = f"Jugador: {result[0]}, Valor máximo: {result[-1]}"
    else:
        result = "No hay jugadores en la lista, agrega uno"
    return result


def salir_programa():
    """
    Función para mostrar el texto de salida del sistema
    :return: Texto de salida
    """
    return print("\nAdios, Gracias!!\n")


def get_player_numeric_input(player_attribute):
    """
    Función para validar si el valor que el usuario ingresa es numérico, si no itera hasta que ingrese un input válido
    :param player_attribute: Recibe el atributo del jugador que vamos a ingresar: dorsal, nombre, etc.
    :return: El input del usuario ingresado
    """
    user_input = input(f"Escribe el {player_attribute} del jugador: ")

    while not is_number(user_input):
        user_input = input(f"El {player_attribute} debe ser un numero: ")
    return user_input


def initialize_game():
    """
    Función principal de inicialización y control de las interacciones
    Muestra el menú principal disponible para el usuario
    De acuerdo al menú seleccionado el sistema llama a las diferentes funciones del programa
    """

    print("Hola, selecciona una opción usando el teclado:"
          "\n[1] Introducir un nuevo jugador",
          "\n[2] Listar jugadores",
          "\n[3] Máximo anotador",
          "\n[4] Estadísticas del equipo",
          "\n[0] Salir del programa")

    user_selection = input("\nEscribe un número de 0 a 4: ")

    if user_selection == "1":

        player_name = input("\nEscribe el nombre del jugador: ")
        player_number = get_player_numeric_input("dorsal")
        player_score_1 = get_player_numeric_input("canastas 1")
        player_score_2 = get_player_numeric_input("canastas 2")
        player_score_3 = get_player_numeric_input("canastas 3")

        new_player = create_nuevo_jugador(
            player_name,
            int(player_number),
            int(player_score_1),
            int(player_score_2),
            int(player_score_3)
        )
        if new_player:
            print("\n==============Creación jugador============")
            print(f"Jugador creado exitosamente {players[-1]}")
            print("==============Fin Creación de Jugadores============\n")
            initialize_game()

    elif user_selection == "2":
        print("\n==============Lista de Jugadores============")
        print(get_jugadores("lista"))
        print("==============Fin lista de Jugadores============\n")
        initialize_game()

    elif user_selection == "3":
        print("\n==============Máximo anotador del equipo============")
        print(get_max_anotador())
        print("==============Fin anotador del equipo===========\n")
        initialize_game()

    elif user_selection == "4":
        print("\n==============Estadísticas de Jugadores============")
        print(get_jugadores("estadistica"))
        print("==============Fin Estadísticas de Jugadores============\n")
        initialize_game()

    elif user_selection == "0":
        salir_programa()
    else:
        print("Seleccionaste una opción que no existe. Intenta de nuevo\n")
        initialize_game()


# Inicializa la aplicación
initialize_game()
