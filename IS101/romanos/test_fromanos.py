from fromanos import a_romanos


def test_simbolos_sencillos():
    assert a_romanos(1) == 'I', "numero incorrecto"
    assert a_romanos(500) == 'D', "numero incorrecto"


def test_doble_repeticion():
    assert a_romanos(2) == 'II'
    assert a_romanos(200) == 'CC'