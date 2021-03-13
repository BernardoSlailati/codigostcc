import sqlite3
from sqlite3 import Error

class BDVeiculo():

    def __init__(self):
        self.conexao = None

        try:
            self.conexao = sqlite3.connect(r"../BancoDeDados/gerencial.db")

        except Error as e:
            print(e)

        self.createTable()

    def createTable(self):
        if self.conexao is not None:
            c = self.conexao.cursor()

            c.execute("""create table if not exists veiculos (
                         idveiculo integer primary key autoincrement ,
                         tipo text,
                         cor text,
                         marca text,
                         modelo text,
                         cpf_proprietario text,
                         ano text);""")
            self.conexao.commit()
            c.close()

        else:
            print("Erro! Impossível acessar banco de dados.")
