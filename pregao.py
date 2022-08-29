from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry, Calendar
from PIL import ImageTk, Image
from time import strftime
from model import *

################# cores ###############

cor0 = "#2e2d2b"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#e06636"   # - profit
cor6 = "#038cfc"   # azul
cor7 = "#3fbfb9"   # verde
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # + verde
cor10 = "#336688"  # azul -

# Configuração da Janela
app = Tk()
app.title('Pregão')
app.geometry('810x535')

# Funções
######## Rélogio########
def time(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

# Listar
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
            tree.delete(*tree.get_children())
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
        b5 = Button(f1, text='Cancelar', width=10, height=1, bg=cor5, command=cancelar)
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

# Frames
f1 = Frame(app, width=810, height=135, relief='flat', bg=cor10)
f1.place(x=0, y=0)

fe = Frame(f1, width=260, height=135, relief='flat', bg=cor2)
fe.place(x=0, y=0)
fp = Frame(f1, width=190, height=75, relief='flat', bg=cor5)
fp.place(x=270, y=10)
fd = Frame(f1, width=330, height=135, relief='flat', bg=cor10)
fd.place(x=470, y=0)

f2 = Frame(app, width=810, height=400, relief='flat', bg=cor3)
f2.place(x=0, y=135)

fle = Frame(f2, width=400, height=900, relief='flat', bg=cor10)
fle.place(x=10, y=10)
fld = Frame(f2, width=245, height=900, relief='flat', bg=cor10)
fld.place(x=565, y=0)

# Entrada
lnome = Label(fe, text='Nome:', bg=cor2)
e_nome = Entry()
ldescricao = Label(fe, text='Descricao:', bg=cor2)
e_descricao = Entry()
ldata = Label(fe, text='Data:', bg=cor2)
e_data = DateEntry(fe)
lvalor = Label(fe, text='Valor R$:', bg=cor2)
e_valor = Entry()
lpesquisar = Label(fd, text='Pesquisar por nome:', bg=cor10, fg=cor1)
e_pesquisar = Entry()

lnome.place(x=20, y=10)
e_nome.place(x=100, y=10)
ldescricao.place(x=20, y=40)
e_descricao.place(x=100, y=40)
ldata.place(x=20, y=70)
e_data.place(x=100, y=70)
lvalor.place(x=20, y=100)
e_valor.place(x=100, y=100)
lpesquisar.place(x=145, y=20)
e_pesquisar.place(x=615, y=45)

# Painel
total = StringVar()
texto= Label(fp,text='Total', width=22, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'))
texto.place(x=-10, y=0)
painel = Label(fp,textvariable=total, width=13, height=1, bg=cor2, fg=cor0, font=('Ivy 20 bold'))
painel.place(x=0, y=25)

# Botões
b1 = Button(fd, text='Cadastrar', width=10, height=1, command=inserir)
b1.place(x=0, y=10)
b2 = Button(fd, text='Atualizar', width=10, height=1, command=confirmar)
b2.place(x=0, y=50)
b3 = Button(fd, text='Deletar', width=10, height=1, command=excluir)
b3.place(x=0, y=90)
b4 = Button(fd, text='Pesquisar', width=10, height=1)
b4.place(x=170, y=80)

# Tree
cols = ('id', 'nome', 'descricao', 'data', 'valor')
tree = ttk.Treeview(fle, columns=cols, show='headings', height=18)

tree.column('id', minwidth=0, width=50)
tree.column('nome', minwidth=0, width=120)
tree.column('descricao', minwidth=0, width=210)
tree.column('data', minwidth=0, width=80)
tree.column('valor', minwidth=0, width=80)

tree.heading('id', text='Cod.')
tree.heading('nome', text='Nome')
tree.heading('descricao', text='Descrição')
tree.heading('data', text='Data')
tree.heading('valor', text='Valor')

vs = ttk.Scrollbar(fle, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll = vs.set)
vs.grid(column=1, row=0, sticky='ns')

tree.grid(column=0, row=0, sticky='ns')

# Calendário
cal = Calendar(fld)
cal.place(x=5, y=55)

# Rélogio
lbl = Label(fld, font = ('calibri', 30, 'bold'), bg = cor0, fg = cor7) 
lbl.place(x=120, y=20, anchor = 'center') 

# Logo
img = ImageTk.PhotoImage(Image.open("caixa.png"))  
l=Label(fld, image=img, bg=cor10)
l.place(x=5, y=230)

# Autor
al = Label(fld, text='by ricardoguita86@gmail.com', bg=cor10, fg=cor1, font=('Ivy 12 bold'))
al.place(x=0,y=370)

time() 
listar()
app.mainloop()