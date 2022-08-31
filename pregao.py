from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry, Calendar
from PIL import ImageTk, Image
from time import strftime
from model import *

######################### Cores #########################

cor0 = "#2e2d2b"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#e06636"   # - profit
cor5 = "#3fbfb9"   # verde
cor6 = "#336688"  # azul -

######################### Configuração da Janela #########################

app = Tk()
app.title('Pregão')
app.geometry('810x535')
app.resizable(False, False)

######################### Funções #########################

def time(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

def listar():
    total_soma = []
    
    for item in consultar():
        #formatando strings
        id = item[0]
        nome = f'{item[1]}'.upper()[:1] + f'{item[1]}'.lower()[1:]
        descricao = f'{item[2]}'.upper()[:1] + f'{item[2]}'.lower()[1:]

        ano = item[3][:4]
        mes = item[3][5:7]
        dia = item[3][8:10]
        
        data = dia+'/'+mes+'/'+ano

        #inserindo dados
        tree.insert('', 0, values=(id, nome, descricao, data, f'R$ {fm(item[4])}'))
        total_soma.append(float(item[4]))

    # Total do Painel     
    tf = sum(total_soma)
    total.set(f'R$ {fm(tf)}')

def inserir():
    nome = e_nome.get()
    descricao = e_descricao.get()
    data = e_data.get_date()
    valor = e_valor.get().replace(',','.')

    try:
        if nome == '' or descricao == '' or data == '' or valor == '':
            messagebox.showinfo(title='Dados Invalidos.', message='Favor preencher todos os campos.')
            return
        try:
            valor = float(valor)
        except:
            messagebox.showinfo(title='Dados Invalidos.', message='campo valor recebe apenas numero.')
            return

        else:
            i = (nome, descricao, data, valor)
            cadastrar(i)
            e_nome.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_valor.delete(0, 'end')

            e_nome.focus()
            tree.delete(*tree.get_children()) # Limpa a treeview
            listar()
            messagebox.showinfo(title='Sucesso', message='Dados cadastrados com sucesso')
    
    except:
        messagebox.showinfo(title='Erro', message='Erro ao cadastrar, nenhum dado foi inserido')

def atualizar():
    global b0, b5, id

    nome = e_nome.get()
    descricao = e_descricao.get()
    data = e_data.get_date()
    valor = e_valor.get().replace(',','.')

    try:
        if nome == '' or descricao == '' or data == '' or valor == '':
            messagebox.showinfo(title='Dados Invalidos.', message='Favor preencher todos os campos.')
            return
        try:
            valor = float(valor)
        except:
            messagebox.showinfo(title='Dados Invalidos.', message='campo valor recebe apenas numero.')
            return

        else:
            i = (nome, descricao, data, valor,id)

            atualizar_form(i)

            e_nome.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_valor.delete(0, 'end')

            e_nome.focus()
            tree.delete(*tree.get_children())
            listar()
            b0.destroy()
            b5.destroy()
            messagebox.showinfo(title='Sucesso', message='Dados atualizado com sucesso')

            b1['state'] = 'normal'
            b2['state'] = 'normal'
            b3['state'] = 'normal'
            b4['state'] = 'normal'
    except:
        messagebox.showinfo(title='Erro', message='Erro ao atualizar, nenhum dado foi atualizado')

def cancelar():
    global b0, b5

    e_nome.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_data.delete(0, 'end')
    e_valor.delete(0, 'end')

    b1['state'] = 'normal'
    b2['state'] = 'normal'
    b3['state'] = 'normal'
    b4['state'] = 'normal'

    b0.destroy()
    b5.destroy()

def confirmar():
    global b0, b5, id

    try:
        selacao = tree.selection()
        item = tree.item(selacao[0])

        id = item['values'][0]
        e_nome.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_data.delete(0, 'end')
        e_valor.delete(0, 'end')

        e_nome.insert(0, item['values'][1])
        e_descricao.insert(0, item['values'][2])
        e_data.insert(0, item['values'][3])
        e_valor.insert(0, f"{item['values'][4]}".replace('R$ ','').replace('.','').replace(',','.').replace('.',','))

        b0 = Button(f1, text='Confirmar', width=10, height=1, bg=cor2, command=atualizar)
        b0.place(x=265, y=102)
        b5 = Button(f1, text='Cancelar', width=10, height=1, bg=cor4, command=cancelar)
        b5.place(x=367, y=102)

        b1['state'] = 'disabled'
        b2['state'] = 'disabled'
        b3['state'] = 'disabled'
        b4['state'] = 'disabled'

    except:
        messagebox.showinfo(title='Aviso', message='Favor selecionar um item')

def excluir():
    try:
        selacao = tree.selection()
        item = tree.item(selacao[0])
        id = item['values'][0]
        nome = item['values'][1]

        confirm = messagebox.askyesno(title='Aviso', message=f'Tem certeza que deseja excluir {nome}?')

        if confirm:
            deletar([id])
            e_nome.focus()
            tree.delete(*tree.get_children())
            listar()
            messagebox.showinfo(title='Sucesso', message='Dados excluido com sucesso')
        else:
            return
    except:
        messagebox.showinfo(title='Aviso', message='Favor selecionar um item')

def pesquizar():
    global escolha, e_pesquisar, p_data

    if escolha.get() == 1:
        nome = e_pesquisar.get()
        resultado = burcar(1, nome)

        if len(resultado) == 0:
            messagebox.showinfo(title='Resultado', message='Resultado não encontrado')
            return

        tree.delete(*tree.get_children())

        total_soma = []
    
        for item in resultado:
            #formatando strings
            id = item[0]
            nome = f'{item[1]}'.upper()[:1] + f'{item[1]}'.lower()[1:]
            descricao = f'{item[2]}'.upper()[:1] + f'{item[2]}'.lower()[1:]

            ano = item[3][:4]
            mes = item[3][5:7]
            dia = item[3][8:10]
            
            data = dia+'/'+mes+'/'+ano

            #inserindo dados
            tree.insert('', 0, values=(id, nome, descricao, data, f'R$ {fm(item[4])}'))
            total_soma.append(float(item[4]))

        # Total do Painel     
        tf = sum(total_soma)
        total.set(f'R$ {fm(tf)}')


    elif escolha.get() == 2:
        data = p_data.get_date()
        resultado = burcar(2, data)

        if len(resultado) == 0:
            messagebox.showinfo(title='Resultado', message='Resultado não encontrado')
            return
        
        tree.delete(*tree.get_children())

        total_soma = []
    
        for item in resultado:
            #formatando strings
            id = item[0]
            nome = f'{item[1]}'.upper()[:1] + f'{item[1]}'.lower()[1:]
            descricao = f'{item[2]}'.upper()[:1] + f'{item[2]}'.lower()[1:]

            ano = item[3][:4]
            mes = item[3][5:7]
            dia = item[3][8:10]
            
            data = dia+'/'+mes+'/'+ano

            #inserindo dados
            tree.insert('', 0, values=(id, nome, descricao, data, f'R$ {fm(item[4])}'))
            total_soma.append(float(item[4]))

        # Total do Painel     
        tf = sum(total_soma)
        total.set(f'R$ {fm(tf)}')

def check(e):
    global e_pesquisar, p_data

    if e == 1:
        p_data.destroy()
        e_pesquisar.destroy()
        e_pesquisar = Entry()
        e_pesquisar.place(x=615, y=55)
    elif e == 2:
        e_pesquisar.destroy()
        p_data = DateEntry(background=cor4)
        p_data.place(x=615, y=55)

#########################  Frame de cima ######################### 

f1 = Frame(app, width=810, height=135, relief='flat', bg=cor6)
f1.place(x=0, y=0)

# Frame esquerdo / Entradas
fe = Frame(f1, width=260, height=135, relief='flat', bg=cor2)
fe.place(x=0, y=0)

# Frame centro / Painel
fp = Frame(f1, width=190, height=75, relief='flat', bg=cor4)
fp.place(x=270, y=10)

# Frame direito / Botões
fd = Frame(f1, width=330, height=135, relief='flat', bg=cor6)
fd.place(x=470, y=0)

#########################  Frame de baixo ######################### 

f2 = Frame(app, width=810, height=400, relief='flat', bg=cor3)
f2.place(x=0, y=135)

# Frame esquerdo / TreeView
fle = Frame(f2, width=400, height=900, relief='flat', bg=cor6)
fle.place(x=10, y=10)

# Frame direito / Calendario, Rélogio, Logo e Author
fld = Frame(f2, width=245, height=900, relief='flat', bg=cor6)
fld.place(x=565, y=0)

######################### Entrada #########################

# Nome
lnome = Label(fe, text='Nome:', bg=cor2) 
e_nome = Entry() 
lnome.place(x=20, y=10)
e_nome.place(x=100, y=10)

# Descrição
ldescricao = Label(fe, text='Descricao:', bg=cor2) 
e_descricao = Entry()
ldescricao.place(x=20, y=40)
e_descricao.place(x=100, y=40)

# Data
ldata = Label(fe, text='Data:', bg=cor2) 
e_data = DateEntry(fe, background=cor4)
ldata.place(x=20, y=70)
e_data.place(x=100, y=70)

# Valor
lvalor = Label(fe, text='Valor R$:', bg=cor2) 
e_valor = Entry()
lvalor.place(x=20, y=100)
e_valor.place(x=100, y=100)

# Pesquisar
lpesquisar = Label(fd, text='Pesquisar por:', bg=cor6, fg=cor1) 
e_pesquisar = Entry()
lpesquisar.place(x=140, y=10)
e_pesquisar.place(x=615, y=55)

# Pesquisar Data
p_data = DateEntry(background=cor4)

# RadiomButtom
escolha = IntVar()
escolha.set(1)

rb1 = Radiobutton(fd, text='Nome', bg=cor6, highlightbackground=cor6, activebackground=cor6, value=1, variable=escolha, command=lambda:check(1))
rb1.place(x=135, y=28)
rb2 = Radiobutton(fd, text='Data', bg=cor6, highlightbackground=cor6, activebackground=cor6, value=2, variable=escolha, command=lambda:check(2))
rb2.place(x=200, y=28)

######################### Painel Total #########################

total = StringVar()

# Texto Total
texto= Label(fp,text='Total', width=22, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold')) 
texto.place(x=-10, y=0)

# Valor no Painel
painel = Label(fp,textvariable=total, width=13, height=1, bg=cor2, fg=cor0, font=('Ivy 20 bold')) 
painel.place(x=0, y=25)

######################### Botões #########################

# Botão Cadastrar
b1 = Button(fd, text='Cadastrar', width=10, height=1, command=inserir) 
b1.place(x=0, y=10)

# Botão Atualizar
b2 = Button(fd, text='Atualizar', width=10, height=1, command=confirmar) 
b2.place(x=0, y=50)

# Botão Deletar
b3 = Button(fd, text='Deletar', width=10, height=1, command=excluir) 
b3.place(x=0, y=90)

# Botão Pesquisar
b4 = Button(fd, text='Pesquisar', width=10, height=1, command=pesquizar) 
b4.place(x=170, y=90)

######################### TreeView #########################

# Configurando colunas no Treeview
cols = ('id', 'nome', 'descricao', 'data', 'valor')
tree = ttk.Treeview(fle, columns=cols, show='headings', height=18)

# Configurando tamanho das colunas no treeview
tree.column('id', minwidth=0, width=50)
tree.column('nome', minwidth=0, width=120)
tree.column('descricao', minwidth=0, width=210)
tree.column('data', minwidth=0, width=80)
tree.column('valor', minwidth=0, width=80)

# Configurando cabeçalho no treeview
tree.heading('id', text='Cod.')
tree.heading('nome', text='Nome')
tree.heading('descricao', text='Descrição')
tree.heading('data', text='Data')
tree.heading('valor', text='Valor')

# Scrollbar
vs = ttk.Scrollbar(fle, orient=VERTICAL, command=tree.yview) 

# Setando scrollbar no treeview
tree.configure(yscroll = vs.set) 

# Mostrar treeview e scrollbar
tree.grid(column=0, row=0, sticky='ns')
vs.grid(column=1, row=0, sticky='ns')

######################### Painel Direito #########################

# Calendário
cal = Calendar(fld, background=cor2)
cal.place(x=5, y=55)

# Rélogio
lbl = Label(fld, font = ('calibri', 30, 'bold'), bg = cor0, fg = cor5) 
lbl.place(x=120, y=20, anchor = 'center') 

# Logo
img = ImageTk.PhotoImage(Image.open("caixa.png"))  
l=Label(fld, image=img, bg=cor6)
l.place(x=5, y=230)

# Autor
al = Label(fld, text='by ricardoguita86@gmail.com', bg=cor6, fg=cor1, font=('Ivy 12 bold'))
al.place(x=0,y=370)

# Iniciando loops
time() 
listar()
app.mainloop()