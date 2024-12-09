import cifrador_cesar


def test_cifrado_simple_3():
    cesar_3 = cifrador_cesar.new_encryptor(3)
    assert cesar_3('ZigZag') == "BLJBDJ"


def test_cifrado_simple_2():
    cesar_2 = cifrador_cesar.new_encryptor(2)
    assert cesar_2('ZigZag') == "AKIACI"


def test_cifrado_reverso():
    reverse_2 = cifrador_cesar.new_encryptor(-2)
    assert reverse_2('akiaci') == "ZIGZAG"
