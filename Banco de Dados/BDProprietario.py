import sqlite3

class BDProprietario():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()


    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists proprietarios (
                     idproprietario integer primary key autoincrement ,
                     nome text,
                     telefone text,
                     apartamento text,
                     visitante text)""")
        self.conexao.commit()
        c.close()