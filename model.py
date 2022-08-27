import sqlite3 as lite

con = lite.connect('database.db') # Conecta ao banco de dados

def cadastrar(i): # Recebe uma Tupla como parâmetro
    with con:
        cursor = con.cursor()
        query = "INSERT INTO dividas(nome, descricao, data, valor) VALUES(?,?,?,?)"
        cursor.execute(query, i)

def consultar(): # Retorna uma Lista
    with con:
        cursor = con.cursor()
        query = cursor.execute("SELECT * FROM dividas")
        itens = query.fetchall()
        return itens

def atualizar_form(i): # Recebe uma Tupla como parâmetro
    with con:
        cursor = con.cursor()
        query = "UPDATE dividas SET nome=?, descricao=?, data=?, valor=? WHERE id=?"
        cursor.execute(query, i)

def deletar(i): # Recebe uma Lista como parâmetro
    with con:
        cursor = con.cursor()
        query = "DELETE FROM dividas WHERE id=?"
        cursor.execute(query, i)

def fm(n): # Formatar Moeda, recebe um numero com parâmetro
    nf = "{:_.2f}".format(float(n)).replace('.',',').replace('_','.')
    return nf