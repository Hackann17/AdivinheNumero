import tkinter as tk
from tkinter import ttk
import NumeroGerado
import Jogada
from Jogada import Jogada as jogada
from tkinter import messagebox


def reiniciar_jogo(janela, TxtBarnumero):
    print('O cara quer jogar de novo kkkk')
    jogada.lista_jogadas.clear()
    Janela.numero_gerado = NumeroGerado.gerar_numero()
    list_l = Janela.list_Txtjogadas
    list_l.clear()
    TxtBarnumero.delete(0, len(TxtBarnumero.get()))

    janela.destroy()

    main()


# esse valor é gerado antes da tela aparecer e nao pode ser modificado no decorrer no codigo em hipotese alguma
class Janela:
    numero_gerado = NumeroGerado.gerar_numero()
    list_Txtjogadas = []


def main():
    janela = tk.Tk()
    janela.title('Adivinhe o número!  ')

    def test():
        num_id = Jogada.analisa_caracteres(TxtBarnumero)

        if num_id == 0:
            n_id = Jogada.compara_numeros(TxtBarnumero.get(), Janela.numero_gerado)
            gera_tabela(jogada.lista_jogadas)
            if n_id == 3:
                mensagens(n_id)

        if num_id == 1:
            mensagens(num_id)

        if num_id == 2:
            mensagens(num_id)

        if num_id == 4:
            mensagens(num_id)

    # Label
    lbcabecalho = tk.Label(janela, text="Algarismos disponiveis:")
    lbcabecalho.grid(column=1, row=0)

    lbnumeros = tk.Label(janela, text='0123456789')
    lbnumeros.grid(column=1, row=1)

    ttk.Label(janela, text='-------------Jogadas-------------').grid(column=1, row=7, padx=10)

    ttk.Label(janela, text='id  | numero sugerido | mesma posição |  outra posição').grid(column=1, row=11, padx=6)

    # Entrada de texto
    TxtBarnumero = tk.Entry(janela)
    TxtBarnumero.grid(column=1, row=2)

    # def click_enter(event):
    # var = event.char() == 'enter'

    # janela.bind('<Key>', click_enter())
    # Button
    bt_testar = tk.Button(janela, text='Conferir números', command=test)
    bt_testar.grid(column=1, row=4)
    # bt_testar.pack()

    btsair = tk.Button(janela, name='btsair', text="Sair", command=janela.destroy)
    btsair.grid(column=1, row=6, padx=4, pady=4)

    # mostra determinada mensagem de acordo com o id de cada uma
    def mensagens(msg_id):
        txt3 = TxtBarnumero.get()

        # Mensagens de erro
        if msg_id == 1:
            TxtBarnumero.insert(0, '')
            messagebox.showinfo(title=None, message='O número sugerido deve ter exatamente 4(quatro) caracteres')

        if msg_id == 2:
            messagebox.showinfo(title=None, message='O número sugerido nao pode conter caracteres repetidos')

        if msg_id == 3:
            resposta = messagebox.askquestion(title=None,
                                              message=f"Pabens voce acertou o número!!\n Numero Sugerido:{txt3} "
                                                      f"\n Numeros Gerado: {Janela.numero_gerado} \n Deseja jogar de "
                                                      f"novo ? ")
            if resposta == 'yes':
                reiniciar_jogo(janela, TxtBarnumero)

            else:
                janela.destroy()

        if msg_id == 4:
            messagebox.showinfo(title=None, message=f'Só sao permitidos números')

    def gera_tabela(lista_jogadas):
        # atributos do objeto :
        # id jogada, numsugerido,mesmap , outrap
        list_txtjogada = Janela.list_Txtjogadas

        for i in range(len(lista_jogadas)):
            jog = lista_jogadas[i]
            list_txtjogada.append(
                tk.Label(janela, text=f' {jog.id_jogada}     |             {jog.numero_sugerido}           | '
                                      f'           {jog.resultados}           ').grid(column=1, row=i + 12))

    janela.mainloop()


main()
