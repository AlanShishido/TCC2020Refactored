import sqlite3

class database:
    nomeTabela = "NutrienteDatabase"
    lista = [
        ["id", "INTEGER PRIMARY KEY AUTOINCREMENT"],
        ["data", "DATE NOT NULL"],
        ["tempo", "TIME NOT NULL"],
        ["condutividade", "INTEGER"],
        ["nivel_ph", "DOUBLE"],
        ["temperatura_ambiente", "INTEGER"],
        ["temperatura_agua", "INTEGER"],
        ["umidade_ambiente", "INTEGER"]
    ]

    def __init__(self):
        pass
    

    def textCriarTabela(self):
        texto = "CREATE TABLE IF NOT EXISTS "
        texto += self.nomeTabela
        texto += " ("
        for data in self.lista:
            for d in data:
                # texto += " "
                texto += d
                texto += " "
            if data != self.lista[-1]:
                texto += " , "
        texto += ");"
        # print(texto)
        return texto

    def textInserirTabela(self):
        texto = "INSERT INTO " + self.nomeTabela + " ("
        for dados in self.lista:
            if dados != self.lista[0]:
                texto += dados[0]
                if dados != self.lista[-1]:
                    texto += ", "
        texto += ") VALUES ("
        for i in range(1,len(self.lista)):
            texto += "?"
            if i != len(self.lista)-1 :
                texto+=","
        texto += ")"
        print (texto)
        return texto

    def dbCriarTabela(self):
        try:
            conn = sqlite3.connect(self.nomeTabela+".db")
            cursor = conn.cursor()
            cursor.execute(self.textCriarTabela())
            print("Tabela Criado")

        except sqlite3.Error as error:
            print("Erro ocorrido:", error)

        finally:
            if (conn):
                conn.close()
                print("Desconectou Conexão com SQLite")

    def dbInserirDados(self,dados):
        try:
            conn = sqlite3.connect(self.nomeTabela+".db")
            cursor = conn.cursor()
            
            cursor.executemany(self.textInserirTabela(), dados)
            conn.commit()
            print("Dados Inseridos")

        except sqlite3.Error as error:
            print("Erro ocorrido:", error)

        finally:
            if (conn):
                conn.close()
                print("Desconectou Conexão com SQLite")

    def dbLerTodosDados(self):

        try:
            conn = sqlite3.connect(self.nomeTabela+".db")
            cursor = conn.cursor()
            
            cursor.execute("""
            SELECT * FROM """+ self.nomeTabela +""";
            """)
            print("leitura")
            for linha in cursor.fetchall():
                print(linha)
                   

        except sqlite3.Error as error:
            print("Erro ocorrido:", error)

        finally:
            if (conn):
                conn.close()
                print("Desconectou Conexão com SQLite")