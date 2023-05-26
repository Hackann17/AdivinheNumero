# link de jogo de referencia https://pt.goobix.com/jogos-online/adivinhar-numero/
from classes_modelo import NumeroGerado
import Janela


class Jogada:
    def __init__(self, id_jogada, numero_proposto, resultados):
        self.id_jogada = id_jogada
        self.numero_proposto = numero_proposto
        self.resultados = resultados


def conta_caracteres(TxtBarnumero):
    num_sug = TxtBarnumero.get()
    repete = False

    if len(num_sug) == 4:
        for i in num_sug:
            if num_sug.count(i) >= 2:
                repete = True

        if repete:
            TxtBarnumero.set('')
            Janela.mensagens(1)
    else:
        TxtBarnumero.set('')
        Janela.mensagens(0)

def analisar_jogada(TxtBarnumero, numero_gerado):
    # Confere se o numero sugerido esta no limite dos caracteres e se tem algum repetido
    conta_caracteres(TxtBarnumero)
    # Algum caractere do numero sugerido é igual ao do gerado?(quantos)
    # Estao na mesma posição ou não?(quantos)
    # Veirificar se sao iguais

    # Gerar objeto da clase jogada e mostra lo na tela em forma de tabela

    print(TxtBarnumero.get(), type(TxtBarnumero.get()))
    print(numero_gerado)
