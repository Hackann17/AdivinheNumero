import random


def gerar_numero():
    num_gerado = str(random.randint(1000, 9999))

    for i in num_gerado:
        if num_gerado.count(i) >= 2:
            num_gerado = ''
            gerar_numero()

    return num_gerado


class NumeroGerado:
    def __init__(self, numero_gerado):
        self.numero_gerado = numero_gerado

    gerar_numero()