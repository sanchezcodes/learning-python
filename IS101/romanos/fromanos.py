numeros_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def traducir(valor: int) -> str:

    pass


def a_romanos(numero: int) -> str:
    lista_traducciones = []

    numero_str = str(numero)
    reves = numero_str[::-1]
    for posicion, cifra in enumerate(reves):
        valor = descomponer(posicion, cifra)
        # valor = lambda p, c: int(c) * 10 ** p
        valor_traducio = traducir(valor)
        lista_traducciones.append(valor_traducio)

    lista_traducciones_inversa = lista_traducciones.reverse()
    num_romano = ""
    for simbolo in lista_traducciones_inversa:
        num_romano += simbolo
    return num_romano


def descomponer(position: int, valor: str) -> str:
    return int(valor) * (10 ** position)


print(descomponer(0, "9"))
