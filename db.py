import sqlite3

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastros (
        nome TEXT,
        idade INTEGER,
        cidade TEXT,
        estado TEXT,
        telefone TEXT,
        email TEXT,
        experiencias TEXT,
        situacao_empregaticia TEXT,
        faixa_salarial TEXT,
        curriculo_path TEXT
    )
''')