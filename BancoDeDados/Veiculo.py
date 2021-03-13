from BancoDeDados.BDVeiculo import BDVeiculo


class Veiculo(object):

    def __init__(self, idveiculo=0, tipo="", cor="", marca="", modelo="", ano="", cpf_proprietario=""):
        self.info = {}
        self.idveiculo = idveiculo
        self.tipo = tipo
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cpf_proprietario = cpf_proprietario

    def inserir(self):

        banco = BDVeiculo()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into veiculos (tipo, cor, marca, modelo, ano, cpf_proprietario) values ('" + self.tipo +
                "', '" + self.cor + "', '" + self.marca + "', '" + self.modelo + "', '" + self.ano + "', '" +
                self.cpf_proprietario + "' )")

            banco.conexao.commit()
            c.close()

            return "Veículo cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do veículo..."

    def atualizar(self):

        banco = BDVeiculo()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "update veiculos set tipo = '" + self.tipo + "', cor = '" + self.cor + "', marca = '" +
                self.marca + "', modelo = '" + self.modelo + "', ano = '" + self.ano + "', cpf_proprietario = '" +
                self.cpf_proprietario + "' where idveiculo = " + str(self.idveiculo) + " ")

            banco.conexao.commit()
            c.close()

            return "Veículo atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do veículo..."

    def deletar(self):

        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from veiculos where idveiculo = " + str(self.idveiculo) + " ")
            banco.conexao.commit()
            c.close()

            return "Veículo excluído com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do veículo..."

    def buscar(self, idveiculo):
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
                self.cpf_proprietario = linha[6]

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do veículo..."

    def buscarTodos(self):
        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from veiculos")

            todos_veiculos = []
            for linha in c:
                todos_veiculos.append(linha)

            c.close()

            return todos_veiculos

        except:
            return "Ocorreu um erro na busca do veículo..."

    def descricao(self):
        return "Tipo: " + str(self.tipo) + " | Cor: " + str(self.cor) + " | Marca: " + str(
            self.marca) + " | Modelo: " + str(self.modelo) + " | Ano: " + str(self.ano) + " | CPF Proprietário: " +\
            self.cpf_proprietario
