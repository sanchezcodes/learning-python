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
group_people = []

TIPO_BILLETE = {
    0: ('GRATIS', 0),
    1: ('NINOS', 14),
    2: ('MAYOR DE 13', 23),
    3: ('MAYOR DE 65', 18)
}


def is_positive_number(edad: str) -> bool:
    return edad.isdigit() and int(edad) >= 0


def get_ticket_type(edad: int) -> int:
    result = 0
    if edad < 3:
        result = 0
    elif edad <= 12:
        result = 1
    elif edad <= 65:
        result = 2
    else:
        result = 3
    return result


# funcion que agrege persopnas al grupo y cuente los tipos y vaya totalizando
# agregar persona al grupo
# contar el tipo de ticket
# total por tipo de tikcet
# total grupo

def get_group_details():
    """
    TODO: Simplificar el obtener el valor de cada tipo no se como unificarlo
    :return:
    """
    result = ""
    gratis = 0
    ninos = 0
    adultos = 0
    jubilados = 0

    for person in group_people:
        tipo, valor = TIPO_BILLETE[person]

        if tipo == TIPO_BILLETE[0][0]:
            gratis = gratis + 1
        elif tipo == TIPO_BILLETE[1][0]:
            ninos = ninos + 1
        elif tipo == TIPO_BILLETE[2][0]:
            adultos = adultos + 1
        elif tipo == TIPO_BILLETE[3][0]:
            jubilados = jubilados + 1

    result += "\n==============DETALLES DEL GRUPO=================\n"
    result += f"Gratis (menores de 2 años):  {gratis} x {TIPO_BILLETE[0][1]} euros = {gratis * TIPO_BILLETE[0][1]} \n"
    result += f"Niños (3-12 años):  {ninos} x {TIPO_BILLETE[1][1]} euros = {ninos * TIPO_BILLETE[1][1]} \n"
    result += f"Adultos (13-64 años):  {adultos} x {TIPO_BILLETE[2][1]} euros = {adultos * TIPO_BILLETE[2][1]} \n"
    result += f"Jubilados (65+ años):  {jubilados} x {TIPO_BILLETE[3][1]} euros = {jubilados * TIPO_BILLETE[3][1]} \n"
    result += "==============FIN DETALLE DEL GRUPO=================\n"
    return result


def get_group_totals() -> int:
    result = 0
    for person in group_people:
        result = result + TIPO_BILLETE[person][1]
    return result


def pedir_edad():
    while True:
        age = input("Introduce la edad del visitante (deja vacío para terminar): ")
        if age == "":
            costo_total = get_group_totals()
            group_details = get_group_details()
            print(f"\n=========TOTAL=========\n"
                  f"Precio total del grupo: {costo_total} euros\n",
                  group_details)
            break
        elif is_positive_number(age):
            tipo = get_ticket_type(int(age))
            group_people.append(tipo)


pedir_edad()
