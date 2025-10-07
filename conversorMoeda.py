import tkinter as tk
from moeda import apiDolar

def dolar():
    cotacao = float(apiDolar())
    reais = float(valor.get())
    conta = round(reais / cotacao,2)
    mensagem = f'R$ {reais:.2f} reais compra-se $ {conta} dólares'
    resposta.config(text=mensagem)
    #return mensagem

janela = tk.Tk()
janela.geometry('500x300')
janela.title('Aula 04 - Tkinter')
janela.configure(bg='#042940')

titulo = tk.Label(janela, text='Conversor de Reais para Dólar', font=('Verdana', 16), fg='#DBF227', bg='#042940')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='Digite valor em Reais para Converter', font=('Verdana',12), fg='#D6D58E', bg='#042940')
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg='#D6D58E', fg='#005C53')
valor.pack(pady=10)

botao = tk.Button(janela, text='CONVERTER', command=dolar , bg='#9FC131', fg='#042940')
botao.pack(pady=10)

resposta = tk.Label(janela, text='', font=('Verdana',12), fg='#D6D58E', bg='#042940')
resposta.pack(pady=10)

janela.mainloop()




