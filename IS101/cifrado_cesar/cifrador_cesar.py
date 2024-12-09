"""La aritmética modular se refiere a las operaciones de suma,
resta, multiplicación y división realizadas en un conjunto
finito de números, donde los resultados se “envuelven” al
alcanzar un cierto valor, llamado módulo. Por ejemplo, en un
reloj de 12 horas, después de las 12 viene la 1, no la 13;
este es un ejemplo cotidiano de aritmética modular con módulo 12

Además del reloj, otro ejemplo de aritmética modular es la operación
 de días de la semana. Si hoy es miércoles y queremos saber qué día
 será en 10 días, sumamos 10 a 3 (porque miércoles es el tercer día),
 lo que da 13. Al aplicar módulo 7, el resultado es 6, que corresponde al sábado.
 Otro ejemplo es en criptografía, donde la aritmética modular se
 usa en algoritmos como RSA para asegurar la seguridad en las comunicaciones.
"""
from typing import Callable

alphabet = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ')


def new_encryptor(d: int) -> Callable:
    def encrypt(message: str) -> str:
        list_message = list(message.upper())  # transformar el string a mayúsculas
        result = ""
        for character in list_message:
            # para cada letra del mensaje
            # busque el indice en la lista de letras y sume d
            # si es el final de la lista busque desde el principio hasta d
            # la operacion % me devuelve el remamente de la división
            #   para A indice 0 + 3 = 3, 3 % del largo de la lista (28) = 3 = D
            #   para Z indice 25 + 3 = 29, 29 % del largo de la lista (28) = 0 = B
            index_of_character = alphabet.index(character) + d  # busque el indice de la lista + d
            new_index = index_of_character % len(alphabet)
            result += alphabet[new_index]
        return result

    return encrypt