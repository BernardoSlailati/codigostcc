import sqlite3
from sqlite3 import Error


class BDEntrada:

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

                c.execute("""CREATE TABLE IF NOT EXISTS entradas (
                             id integer PRIMARY KEY autoincrement,
                             data_hora datetime,
                             proprietario text,
                             veiculo text,
                             visitante text,
                             placa text
                             );""")

                self.conexao.commit()

                c.close()
            except Error as e:
                print(e)

        else:
            print("Erro! Impossível acessar banco de dados.")
