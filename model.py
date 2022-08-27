import sqlite3 as lite

con = lite.connect('database.db')

def cadastrar(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO dividas(nome, descricao, data, valor) VALUES(?,?,?,?)"
        cursor.execute(query, i)

def consultar():
    with con:
        cursor = con.cursor()
        query = cursor.execute("SELECT * FROM dividas")
        itens = query.fetchall()
        return itens

def atualizar_form(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE dividas SET nome=?, descricao=?, data=?, valor=? WHERE id=?"
        cursor.execute(query, i)

def deletar(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM dividas WHERE id=?"
        cursor.execute(query, i)

def fm(n): # Formatar Moeda
    nf = "{:_.2f}".format(float(n)).replace('.',',').replace('_','.')
    return nf