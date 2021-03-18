import sqlite3
from sqlite3 import Error


class BDProprietario:

    def __init__(self):
        self.conexao = None

        try:
            self.conexao = sqlite3.connect(r"..\BancoDeDados\gerencial.db")
        except Error as e:
            print(e)

        self.createTable()

    def createTable(self):
        if self.conexao is not None:
            try:
                c = self.conexao.cursor()

                c.execute("""CREATE TABLE IF NOT EXISTS proprietarios (
                             id integer PRIMARY KEY autoincrement,
                             nome text,
                             cpf text,
                             telefone text,
                             apartamento text,
                             visitante text
                             );""")

                self.conexao.commit()

                c.close()
            except Error as e:
                print(e)

        else:
            print("Erro! Impossível acessar banco de dados.")
