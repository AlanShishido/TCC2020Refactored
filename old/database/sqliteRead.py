#desenvolvimento de código para o trabalho da faculdade

import sqlite3

try:
    conn = sqlite3.connect('clientes.db')
    print("Conectado com SQLite")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT * FROM clientes;
    """)

    for linha in cursor.fetchall():
        print(linha)    

except sqlite3.Error as error:
    print("Erro ocorrido:", error)

finally:
    if (conn):
        conn.close()
        print("Desconectou Conexão com SQLite")