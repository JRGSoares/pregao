import sqlite3 as lite

con = lite.connect('database.db')

with con:
    cursor = con.cursor()
    query = '''CREATE TABLE dividas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        descricao VARCHAR(100),
        data DATE,
        valor DECIMAL
    )'''
    cursor.execute(query)