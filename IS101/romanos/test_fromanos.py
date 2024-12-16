from fromanos import a_romanos, descomponer


def test_simbolos_sencillos():
    assert a_romanos(1) == 'I', "numero incorrecto"
    assert a_romanos(500) == 'D', "numero incorrecto"


def test_doble_repeticion():
    assert a_romanos(2) == 'II'
    assert a_romanos(200) == 'CC'


def test_descomponer():
    # voy a probar el numero 1939, cadena '9391'
    resultado = descomponer(0, '9')
    assert resultado == 9
    resultado = descomponer(1, '3')
    assert resultado == 30
    resultado = descomponer(2, '9')
    assert resultado == 900
    resultado = descomponer(3, '1')
    assert resultado == 1000

def test_traducir():
    assert traducir(9) == 'IX'
    assert traducir(30) == 'XXX'
    assert traducir(900) == 'CM'
    assert traducir(1000) == 'M'