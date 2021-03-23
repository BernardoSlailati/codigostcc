from BancoDeDados.BDVeiculo import BDVeiculo


class Veiculo(object):

    def __init__(self, idveiculo=0, tipo="", cor="", marca="", modelo="", ano="", placa="", cpf_proprietario=""):
        self.info = {}
        self.idveiculo = idveiculo
        self.tipo = tipo
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cpf_proprietario = cpf_proprietario

    def inserir(self):

        banco = BDVeiculo()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into veiculos (tipo, cor, marca, modelo, ano, placa, cpf_proprietario) values ('" + self.tipo +
                "', '" + self.cor + "', '" + self.marca + "', '" + self.modelo + "', '" + self.ano + "', '" +
                self.placa + "', '" + self.cpf_proprietario + "' )")

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
                "update veiculos set tipo = '" + self.tipo + "', cor = '" + self.cor + "', marca = '" + self.marca +
                "', modelo = '" + self.modelo + "', ano = '" + self.ano + "', placa = '" + self.placa +
                "', cpf_proprietario = '" + self.cpf_proprietario + "' where id = " + str(self.idveiculo) + " ")

            banco.conexao.commit()
            c.close()

            return "Veículo atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do veículo..."

    def deletar(self):

        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from veiculos where id = " + str(self.idveiculo))
            banco.conexao.commit()
            c.close()

            return "Veículo excluído com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do veículo..."

    def buscar(self, idveiculo):
        banco = BDVeiculo()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from veiculos where id = " + str(idveiculo) + "  ")

            for linha in c:
                self.idveiculo = linha[0]
                self.tipo = linha[1]
                self.cor = linha[2]
                self.marca = linha[3]
                self.modelo = linha[4]
                self.ano = linha[5]
                self.placa = linha[6]
                self.cpf_proprietario = linha[7]

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do veículo..."

    def pesquisar(self, tipoPesquisa, valorPesquisa):

        banco = BDVeiculo()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from veiculos where lower(" + str(tipoPesquisa).lower().replace(" ", "_").replace("á", "a") +
                      ") = '" + str(valorPesquisa).lower() + "' order by id limit 1")

            for linha in c:
                self.idveiculo = linha[0]
                self.tipo = linha[1]
                self.cor = linha[2]
                self.marca = linha[3]
                self.modelo = linha[4]
                self.ano = linha[5]
                self.placa = linha[6]
                self.cpf_proprietario = linha[7]

            c.close()

            return self

        except:
            return None

    def buscarTodos(self):

        banco = BDVeiculo()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from veiculos order by id")

            todos_proprietarios = []
            for linha in c:

                todos_proprietarios.append(Veiculo(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5],
                    linha[6],
                    linha[7]
                ))

            c.close()

            return todos_proprietarios

        except:
            return "Ocorreu um erro na busca de todos os proprietários..."

    def descricao(self):
        return "Tipo: " + str(self.tipo) + " | Cor: " + str(self.cor) + " | Marca: " + str(
            self.marca) + " | Modelo: " + str(self.modelo) + " | Ano: " + str(self.ano) + " Placa: " + self.placa + \
               " | CPF Proprietário: " + self.cpf_proprietario
