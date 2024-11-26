"""
Se dispondrá de un menú que ofrecerá las siguientes opciones al usuario:
[1] Introducir un nuevo jugador
[2] Listar jugadores
[3] Máximo anotador
[4] Estadísticas del equipo
[0] Salir del programa

Requisitos mínimos
Modularización: Es imprescindible generar al menos 3 funciones para resolver cualquiera de las problemáticas propuestas
Uso de colecciones: Es imprescindible usar al menos un tipo de colecciones propuestas en el curso
Comentarios: Es imprescindible comentar como mínimo todas las funciones definidas así como los bloques más importantes
Buenas prácticas: Es imprescindible que el nombre de las variables y funciones siga unas buenas prácticas de definición
"""

"""
Definición del jugador
- Función Introducir un nuevo jugador
-- debe validar que el dorsal no esta repetido
-- la función debe recibir nombre, dorsal, canastas_3, canastas_2, canastas_1
-- debo guardar los jugadores en una lista
-- al guardar los valores sumar las canastas y guardar el total
-- las lista debe tener todos los datos de los jugadores.

- Función Listar los jugadores 
-- obtener toda la lista
-- obtener la lista por jugador
-- en este listado las anotaciones deben ser totales por jugador

- Función Máximo Anotador
-- Sumar los totales de las canastas de 3, 2 y 1 de cada jugador, devolver el jugador con el numero mayor

- Función Estadísticas del equipo
-- Listar todos los jugadores con los valores de cada canasta y el total 

- Función Salir del Programa
"""
players = []


def is_player_duplicated(dorsal):
    """
    Función que verifica si un jugador ya fue ingresado con ese mismo dorsal
    :param dorsal: int number of the player
    :return: True if player exist or False if not exist
    """
    result = False
    if dorsal in players:
        result = True
    return result


def is_string(text):
    text = str(text)
    return isinstance(text, str)


def is_number(number):
    return number.isdigit()

def is_empty(value):
    return value == ''


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


def get_player(dorsal):
    result = []
    return players[dorsal]


def create_nuevo_jugador(nombre, dorsal, canastas_1, canastas_2, canastas_3):
    result = ""
    if is_player_duplicated(dorsal):
        result = "El jugador ya ha sido ingresado en la lista, intenta de nuevo."
    else:
        players.append([nombre, dorsal, canastas_1, canastas_2, canastas_3])
        result = "Jugador ha sido agregado en la lista correctamente"
    return result


def get_lista_jugadores():
    return players


def get_maximo_anotador():
    result = []
    return result


def get_estadisticas_equipo():
    result = []
    return result


def salir_programa():
    result = ""
    return result


def get_player_numeric_input(player_attribute):
    user_input = input(f"Escribe el {player_attribute} del jugador: ")
    while not is_number(user_input):
        user_input = input(f"El {player_attribute} debe ser un numero: ")
    return user_input

def initialize_game():
    print("Hola, selecciona una opción usando el teclado:"
          "\n[1] Introducir un nuevo jugador",
          "\n[2] Listar jugadores",
          "\n[3] Máximo anotador",
          "\n[4] Estadísticas del equipo",
          "\n[0] Salir del programa")

    user_selection = input("Escribe un número de 0 a 4: ")

    if user_selection == "1":

        player_name = input("Escribe el nombre del jugador: ")

        player_number = get_player_numeric_input("dorsal")

        player_score_1 = get_player_numeric_input("canastas 1")

        player_score_2 = get_player_numeric_input("canastas 2")

        player_score_3 = get_player_numeric_input("canastas 3")

        create_nuevo_jugador(
            player_name,
            int(player_number),
            int(player_score_1),
            int(player_score_2),
            int(player_score_3)
        )
        print(get_lista_jugadores())

    elif user_selection == "2":
        get_lista_jugadores()

    elif user_selection == "3":
        get_maximo_anotador()

    elif user_selection == "4":
        get_estadisticas_equipo()

    elif user_selection == "0":
        print("Gracias!!\n")
    else:
        print("Seleccionaste una opción que no existe. Intenta de nuevo\n")
        initialize_game()
    return user_selection


initialize_game()
