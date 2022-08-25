from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
from PIL import ImageTk, Image
from time import strftime

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

# Frames
f1 = Frame(app, width=810, height=135, relief='flat', bg=cor10)
f1.place(x=0, y=0)

fe = Frame(f1, width=260, height=135, relief='flat', bg=cor2)
fe.place(x=0, y=0)
fp = Frame(f1, width=150, height=75, relief='flat', bg=cor5)
fp.place(x=290, y=10)
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
texto= Label(fp,text='Total', width=19, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'))
texto.place(x=-10, y=0)
painel = Label(fp,text='R$ 0,00', width=10, height=1, bg=cor2, fg=cor0, font=('Ivy 20 bold'))
painel.place(x=0, y=25)

# Botões
b0 = Button(f1, text='Confirmar', width=10, height=1, bg=cor2)
b0.place(x=265, y=102)
b1 = Button(fd, text='Cadastrar', width=10, height=1)
b1.place(x=0, y=10)
b2 = Button(fd, text='Atualizar', width=10, height=1)
b2.place(x=0, y=50)
b3 = Button(fd, text='Deletar', width=10, height=1)
b3.place(x=0, y=90)
b4 = Button(fd, text='Pesquisar', width=10, height=1)
b4.place(x=170, y=80)

# Tree
cols = ('nome', 'descricao', 'data', 'valor')
tree = ttk.Treeview(fle, columns=cols, show='headings', height=18)

tree.column('nome', minwidth=0, width=150)
tree.column('descricao', minwidth=0, width=210)
tree.column('data', minwidth=0, width=90)
tree.column('valor', minwidth=0, width=80)

tree.heading('nome', text='Nome')
tree.heading('descricao', text='Descrição')
tree.heading('data', text='Data')
tree.heading('valor', text='Valor')

vs = ttk.Scrollbar(fle, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll = vs.set)
vs.grid(column=1, row=0, sticky='ns')

tree.grid(column=0, row=0, sticky='ns')

for _ in range(50):
    tree.insert('', 'end', values=('João da Barraca', 'materiais de limpeza', '24/08/2022', 'R$ 50,00'))

# Calendário
cal = Calendar(fld)
cal.place(x=5, y=55)

# Rélogio
lbl = Label(fld, font = ('calibri', 30, 'bold'), 
            background = cor0, 
            foreground = cor7) 
lbl.place(x=120, y=20, anchor = 'center') 

# Logo
img = ImageTk.PhotoImage(Image.open("caixa.png"))  
l=Label(fld, image=img, bg=cor10)
l.place(x=5, y=245)

time() 
app.mainloop()