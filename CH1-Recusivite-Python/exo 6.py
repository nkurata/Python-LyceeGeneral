def nombre_de_chiffres(n):
    if n<10:
        return 1
    return 1 + nombre_de_chiffres(n//10)
assert nombre_de_chiffres(34126) == 5
assert nombre_de_chiffres(0) == 1