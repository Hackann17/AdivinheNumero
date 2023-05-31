# link de jogo de referencia https://pt.goobix.com/jogos-online/adivinhar-numero/
import Janela


class Jogada:
    def __init__(self, id_jogada, numero_sugerido, resultados):
        self.id_jogada = id_jogada
        self.numero_sugerido = numero_sugerido
        self.resultados = resultados

    lista_jogadas = []

# confere se o numero sugerido se encaixa no padrão
def analisa_caracteres(TxtBarnumero):
    num_sug = str(TxtBarnumero.get())
    repete = False
    carac_nao_num = '!@#$%¨&*()_| <,>.;/?}]{[^+='

    # verifica se há aalgum caracter especial
    for i in num_sug:
        for c in carac_nao_num:
            if i == c:
                TxtBarnumero.delete(0, len(num_sug))
                return 4
        # se tem alguma letra
        if i.isalpha():
            TxtBarnumero.delete(0, len(num_sug))
            return 4
    # verifica se o comprimento do numero é maior ou menor que 4, e se ha alguma repetição
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
def compara_numeros(num_sugerido, num_gerado):
    qtd_algarismos_mesmap = 0
    qtd_algarismos_outrap = 0

    # Veirificar se sao iguais
    if num_gerado == num_sugerido:
        Janela.mensagens(3)
        return True

    elif num_gerado != num_sugerido:
        # Algum algarismo esta na mesma posição ou não?(quantos)
        for n in num_gerado:
            if num_sugerido.count(n) == 1:
                if num_sugerido.index(n) == num_gerado.index(n):
                    qtd_algarismos_mesmap += 1
                else:
                    qtd_algarismos_outrap += 1

        # Gerar lista de objetos da clase jogada e mostra lo na tela em forma de tabela

        jogada = Jogada(len(Jogada.lista_jogadas) + 1, numero_sugerido=num_sugerido,
                        resultados=f' {qtd_algarismos_mesmap}'
                                   f'               |               {qtd_algarismos_outrap}')
        Jogada.lista_jogadas.append(jogada)
