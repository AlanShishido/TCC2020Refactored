#desenvolvimento de código para o trabalho da faculdade

import sqlite3

try:
    conn = sqlite3.connect('clientes.db')
    print("Conectado com SQLite")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf     VARCHAR(11) NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
            cidade TEXT,
            uf VARCHAR(2) NOT NULL,
            criado_em DATE NOT NULL
    );
    """)

except sqlite3.Error as error:
    print("Erro ocorrido:", error)

finally:
    if (conn):
        conn.close()
        print("Desconectou Conexão com SQLite")