from BDVeiculo import BDVeiculo


class Veiculo(object):

    def __init__(self, idveiculo=0, tipo="", cor="", marca="", modelo="", ano=""):
        self.info = {}
        self.idveiculo = idveiculo
        self.tipo = tipo
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def insertUser(self):

        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into veiculos (tipo, cor, marca, modelo, ano) values ('" + self.tipo + "', '" + self.cor + "', '" + self.marca + "', '" + self.modelo + "', '" + self.ano + "' )")

            banco.conexao.commit()
            c.close()

            return "Veículo cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do veículo..."

    def updateUser(self):

        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "update veiculos set tipo = '" + self.tipo + "', cor = '" + self.cor + "', marca = '" + self.marca + "', modelo = '" + self.modelo + "', ano = '" + self.ano + "' where idveiculo = " + self.idveiculo + " ")

            banco.conexao.commit()
            c.close()

            return "Veículo atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do veículo..."

    def deleteUser(self):

        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from veiculos where idveiculo = " + self.idveiculo + " ")
            banco.conexao.commit()
            c.close()

            return "Veículo excluído com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do veículo..."

    def selectUser(self, idveiculo):
        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from veiculos where idveiculo = " + idveiculo + "  ")

            for linha in c:
                self.idveiculo = linha[0]
                self.tipo = linha[1]
                self.cor = linha[2]
                self.marca = linha[3]
                self.modelo = linha[4]
                self.ano = linha[5]

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do veículo..."
