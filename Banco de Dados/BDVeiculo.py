import sqlite3

class BDVeiculo():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()


    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists veiculos (
                     idveiculo integer primary key autoincrement ,
                     tipo text,
                     cor text,
                     marca text,
                     modelo text,
                     ano text)""")
        self.conexao.commit()
        c.close()