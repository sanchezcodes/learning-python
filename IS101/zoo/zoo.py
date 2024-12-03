age = 0
group_people = []


catalogo_entradas = {
    'GRATIS': {"precio": 0, "edad_umbral": 3},
    'NINOS': {"precio": 14, "edad_umbral": 13},
    'ADULTOS': {"precio": 23, "edad_umbral": 65},
    'JUBILADOS': {"precio": 18, "edad_umbral": float('inf')},
}

factura = {
    'GRATIS': 0,
    'NINOS': 0,
    'ADULTOS': 0,
    'JUBILADOS': 0,
}


def is_positive_number(edad: str) -> bool:
    return edad.isdigit() and int(edad) >= 0


def get_ticket_type(edad: int) -> tuple:
    precio = 0
    tipo = 0

    for tipo in catalogo_entradas:
        if edad < catalogo_entradas[tipo]['edad_umbral']:
            precio = catalogo_entradas[tipo]['precio']
            break

    return tipo, precio


def get_group_details():
    result = ""
    precio_total = 0
    numero_entradas = 0

    for tipo, valor in group_people:
        precio_total = precio_total + valor
        factura[tipo] += 1

    for clave in factura:
        print(f" {factura[clave]:2d} entradas {clave.lower()}: {factura[clave] * catalogo_entradas[clave]['precio']:6.2f} €")

    numero_entradas = len(group_people)
    print(f" Número de entradas: {numero_entradas:03d} €")
    print(f" Precio total......: {precio_total:.2f}")
    return result


while True:
    age = input("Introduce la edad del visitante (deja vacío para terminar): ")
    if age == "":
        break
    elif is_positive_number(age):
        tipo = get_ticket_type(int(age))
        group_people.append(tipo)

get_group_details()


