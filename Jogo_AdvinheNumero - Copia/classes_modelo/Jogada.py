# link de jogo de referencia https://pt.goobix.com/jogos-online/adivinhar-numero/
from classes_modelo import NumeroGerado
import Janela
import tkinter


class Jogada:
    def __init__(self, id_jogada, numero_sugerido, resultados):
        self.id_jogada = id_jogada
        self.numero_sugerido = numero_sugerido
        self.resultados = resultados

    lista_jogada = []


# confere se o numero sugerido se encaixa no padrão
def analisa_caracteres(TxtBarnumero, num_gerado):
    num_sug = TxtBarnumero.get()
    repete = False

    if len(num_sug) == 4:
        for i in num_sug:
            if num_sug.count(i) >= 2:
                repete = True
        if repete:
            # se algum numero repetir
            return 2
        else:
            return 0
    else:
        # se nao houver caracteres o suficiente
        return 1


# compara se o numero gerado e o sugerido sao iguais:
def compara_numeros( num_sugerido, num_gerado):
    qtd_algarismos_mesmap = 0
    qtd_algarismos_outrap = 0

    # Veirificar se sao iguais
    if num_gerado == num_sugerido:
        Janela.mensagens(3)
        return True

    elif num_gerado != num_sugerido:
        print('caiu no elif', num_gerado)
        # Algum algarismo esta na mesma posição ou não?(quantos)
        for n in num_gerado:
            if num_sugerido.count(n) == 1:
                if num_sugerido.index(n) == num_gerado.index(n):
                    qtd_algarismos_mesmap += 1
                else:
                    qtd_algarismos_outrap += 1

        # Gerar lista de objetos da clase jogada e mostra lo na tela em forma de tabela

        jogada = Jogada(len(Jogada.lista_jogada), numero_sugerido=num_sugerido,
                        resultados=f'Na mesma posição:{qtd_algarismos_mesmap}'
                                   f' \n Em outra posição:{qtd_algarismos_outrap}')

        print(jogada.id_jogada, jogada.numero_sugerido, jogada.resultados)
        return jogada.lista_jogada.append(jogada)



