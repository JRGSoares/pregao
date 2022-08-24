from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

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

# Configuração da Janela
app = Tk()
app.title('Pregão')
app.geometry('800x500')

# Frames
f1 = Frame(app, width=800, height=135, relief='flat', bg=cor1)
f1.place(x=0, y=0)
f2 = Frame(app, width=800, height=300, relief='flat')
f2.place(x=0, y=135)

# Entrada
lnome = Label(f1, text='Nome:', bg=cor1)
e_nome = Entry()
ldescricao = Label(f1, text='Descricao:', bg=cor1)
e_descricao = Entry()
ldata = Label(f1, text='Data:', bg=cor1)
e_data = DateEntry(f1)
lvalor = Label(f1, text='Valor:', bg=cor1)
e_valor = Entry()

lnome.place(x=20, y=10)
e_nome.place(x=100, y=10)
ldescricao.place(x=20, y=40)
e_descricao.place(x=100, y=40)
ldata.place(x=20, y=70)
e_data.place(x=100, y=70)
lvalor.place(x=20, y=100)
e_valor.place(x=100, y=100)

# Painel
painel = Label(f1,text='R$ 0,00', width=10, height=2, bg=cor2, fg=cor0, font=('Ivy 20 bold'))
painel.place(x=300, y=30)

app.mainloop()