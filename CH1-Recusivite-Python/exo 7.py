def nombre_de_bits(n):
    if n<2:
        return 1
    return 1 + nombre_de_bits(n//2)
assert nombre_de_bits == 8
    