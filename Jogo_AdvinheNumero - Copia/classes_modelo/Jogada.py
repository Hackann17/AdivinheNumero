# link de jogo de referencia https://pt.goobix.com/jogos-online/adivinhar-numero/
from classes_modelo import Numero_Gerado
class Jogada:
    def __init__(self, id_jogada, numero_proposto, resultados):
        self.id_jogada = id_jogada
        self.numero_proposto = numero_proposto
        self.resultados = resultados


def comparar_numero_sugerido(numero_sugerido, numero_gerado):
    print(numero_sugerido, type(numero_sugerido))
    print(numero_gerado)
