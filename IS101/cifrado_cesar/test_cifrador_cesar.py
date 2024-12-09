import cifrador_cesar

cesar_3 = cifrador_cesar.new_encryptor(3)
assert cesar_3('ZigZag') == "BLJBDJ"

cesar_2 = cifrador_cesar.new_encryptor(2)
assert cesar_2('ZigZag') == "AKIACI"

reverse_2 = cifrador_cesar.new_encryptor(-2)
assert reverse_2('akiaci') == "ZIGZAG"
