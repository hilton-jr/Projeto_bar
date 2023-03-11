from struct import pack
import tkinter as tk
from func_bar import*
fundoTela = '#35a1c5'
fundoBotao = '#0022a5e'
letra = 'whigt'
fonte = 'Arial'
largBotao ='20'

def fn_Abrir_Conta():
    jnlConta = tk.Tk()
    jnlConta.geometry('600x300')
    jnlConta.title('Abertura de conta')
    jnlConta.config(bg=fundoTela)

    lbMesa = tk.Label(jnlConta, text='Mesa',font=fonte)
    entMesa = tk.Entry(jnlConta)
    btAbrirConta = tk.Button(jnlConta,text='Abrir Conta',
                            bg=fundoBotao,fg=letra,font=fonte,pad=5,width=largBotao,
                            command=fn_cadastraConta)
    btFim = tk.Button(jnlConta,text='Fechar Janela',
                            bg=fundoBotao,fg=letra,font=fonte,pad=5,width=largBotao,
                            command=jnlConta.destroy)
    

    lbMesa.pack(pady=10)
    entMesa.pack(pady=10)
    btFim.pack(pady=10)

def fn_Inc_Pedido():
    pass

def fn_Exc_Pedido():
    pass

def fn_Fechar_Conta():
    pass


def app():
    jnlPrincipal = tk.Tk()
    jnlPrincipal.geometry('300x600')
    jnlPrincipal.title('Buteco')
    jnlPrincipal.config(bg=fundoTela)


    btAbrirConta = tk.Button(jnlPrincipal,text='Abrir Conta',
                            bg=fundoBotao,fg=letra,pad=5,width=largBotao,
                            command=fn_Abrir_Conta)

    btIncPedido = tk.Button(jnlPrincipal,text='Incluir Pedido',
                            bg=fundoBotao,fg=letra,pad=5,width=largBotao,
                            command=fn_Inc_Pedido)

    btExcPedido = tk.Button(jnlPrincipal,text='Excluir Pedido',
                            bg=fundoBotao,fg=letra,pad=5,width=largBotao, 
                            command=fn_Exc_Pedido)

    btFecharConta = tk.Button(jnlPrincipal,text='Fechar Conta',
                            bg=fundoBotao,fg=letra,pad=5,width=largBotao,
                            command=fn_Fechar_Conta)

    btFecharConta = tk.Button(jnlPrincipal,text='Fechar Conta',
                            bg=fundoBotao,fg=letra,pad=5,width=largBotao,
                            command=fn_Fechar_Conta)



    if __name__ =='__main__':
        app()
    else:
        print("Não é o moduo prinipal")
        exit()