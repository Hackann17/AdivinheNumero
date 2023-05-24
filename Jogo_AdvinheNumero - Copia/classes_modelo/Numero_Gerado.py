import random
def gerar_numero():
    return Numero_Gerado(random.randint(1000, 9999)).numero_gerado

class Numero_Gerado:
    def __init__(self, numero_gerado):
        self.numero_gerado = numero_gerado
