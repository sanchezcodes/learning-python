"""
validar que sea entero positivo
pedir edades de varias personas
reglas de los precios
    si es menor de 2 años
    si es mayor de 2 años a 12 años
    si es mayor de 13 años
    si es mayor de 65 años
calcular el desglose
imprimir el resultado
"""
age = 0

TIPO_BILLETE = {
    0: ('GRATIS', 0),
    1: ('NINOS', 14),
    2: ('MAYOR DE 13', 23),
    3: ('MAYOR DE 65', 18)
}


def is_positive_number(edad: str) -> bool:
    return edad.isdigit() and int(edad) >= 0


def calculo_billete_tipo(edad: int) -> tuple:
    result = []
    if edad < 3:
        result = TIPO_BILLETE[0]
    elif edad <= 12:
        result = TIPO_BILLETE[1]
    elif edad <= 65:
        result = TIPO_BILLETE[2]
    else:
        result = TIPO_BILLETE[3]
    return result


def pedir_edad():
    while True:
        age = input("cuantos años tienes: ")
        if age == "":
            break
        elif is_positive_number(age):
            print(calculo_billete_tipo(int(age)))


pedir_edad()