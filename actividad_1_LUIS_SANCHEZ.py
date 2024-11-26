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


# Utilities

def is_player_duplicated(dorsal):
    """
    :param dorsal: int number of the player
    :return: True if player exist or False if not exist
    """
    result = False
    if dorsal in players:
        result = True
    return result


def sum_all_scores(canastas_1, canastas_2, canastas_3):
    """
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


print(create_nuevo_jugador("luis", 3, 2, 1, 0))


def get_lista_jugadores():
    result = []
    return result


def get_maximo_anotador():
    result = []
    return result


def get_estadisticas_equipo():
    result = []
    return result


def salir_programa():
    result = ""
    return result
