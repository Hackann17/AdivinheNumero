import tkinter as tk
from tkinter import ttk
import NumeroGerado
import Jogada
from Jogada import Jogada as jogada
from tkinter import messagebox

id_jog = 0


# esse valor é gerado antes da tela aparecer e nao pode ser modificado no decorrer no codigo em hipotese alguma
class Janela:
    numero_gerado = NumeroGerado.gerar_numero()
    list_Txtjogadas = []


janela = tk.Tk()
janela.title('Adivinhe o número!  ')
# Label
Lbcabecalho = tk.Label(janela, text="Algarismos disponiveis:")
Lbcabecalho.grid(column=1, row=0)

Lbnumeros = tk.Label(janela, text='0123456789')
Lbnumeros.grid(column=1, row=1)

ttk.Label(janela, text='-------------Jogadas-------------').grid(column=1, row=7, padx=10)

ttk.Label(janela, text='id  | numero sugerido | mesma posição |  outra posição').grid(column=1, row=11, padx=6)

# Entrada de texto
TxtBarnumero = tk.Entry(janela)
TxtBarnumero.grid(column=1, row=2)


def test():
    num_id = Jogada.analisa_caracteres(TxtBarnumero)

    if num_id == 0:
        Jogada.compara_numeros(TxtBarnumero.get(), Janela.numero_gerado)
        gera_tabela(jogada.lista_jogadas)

    if num_id == 1:
        mensagens(num_id)

    if num_id == 2:
        mensagens(num_id)

    if num_id == 4:
        mensagens(num_id)


# Button
BtTestar = tk.Button(janela, text='Conferir números', command=test)
BtTestar.grid(column=1, row=4)

Btsair = tk.Button(janela, name='btsair', text="Sair", command=janela.destroy)
Btsair.grid(column=1, row=6, padx=4, pady=4)


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
                                                  f"\n Numeros Gerado: {Janela.numero_gerado} \n Deseja jogar de novo ? ")
        if resposta == 'yes':
            print('O cara quer jogar de novo kkkk')
            jogada.lista_jogadas.clear()
            Janela.numero_gerado = NumeroGerado.gerar_numero()
            list_l = Janela.list_Txtjogadas
            list_l.clear()
            TxtBarnumero.delete(0, len(TxtBarnumero.get()))

        else:
            janela.destroy()

    if msg_id == 4:
        messagebox.showinfo(title=None, message=f'Só sao permitidos números')


def gera_tabela(lista_jogadas):
    # atributos do objeto :
    # id jogada, numsugerido,mesmap , outrap
    for i in range(len(lista_jogadas)):
        jog = lista_jogadas[i]
        Janela.list_Txtjogadas.append(
            tk.Label(janela, text=f' {jog.id_jogada}     |             {jog.numero_sugerido}           | '
                                  f'           {jog.resultados}           ').grid(column=1, row=i + 12))


janela.mainloop()
