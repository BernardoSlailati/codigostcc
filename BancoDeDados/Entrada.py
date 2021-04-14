from BancoDeDados.BDEntrada import BDEntrada


class Entrada(object):

    def __init__(self, idEntrada=0, data_hora="", proprietario="", veiculo="", visitante="", placa=""):
        self.info = {}
        self.idEntrada = idEntrada
        self.data_hora = data_hora
        self.proprietario = proprietario
        self.veiculo = veiculo
        self.visitante = visitante
        self.placa = placa

    def inserir(self):

        banco = BDEntrada()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into entradas (data_hora, proprietario, veiculo, visitante, placa) values ('" + self.data_hora +
                "', '" + self.proprietario + "', '" + self.veiculo + "', '" + self.visitante + "', '" + self.placa +
                "' )")

            banco.conexao.commit()
            c.close()

            return "Entrada cadastrada com sucesso!"

        except:
            return "Ocorreu um erro na inserção da entrada..."

    def atualizar(self):

        banco = BDEntrada()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "update entradas set data_hora = '" + self.data_hora + "', proprietario = '" + self.proprietario +
                "', veiculo = '" + self.veiculo + "', visitante = '" + self.visitante + "', placa = '" + self.placa +
                "' where id = " + str(self.idEntrada) + " ")

            banco.conexao.commit()
            c.close()

            return "Entrada atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração da entrada..."

    def deletar(self, id):

        banco = BDEntrada()

        try:

            c = banco.conexao.cursor()

            c.execute("delete from entradas where id = " + str(id))
            banco.conexao.commit()
            c.close()

            return "Entrada excluída com sucesso!"

        except:
            return "Ocorreu um erro na exclusão da entrada..."

    def buscar(self, idEntrada):

        banco = BDEntrada()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from entradas where id = " + str(idEntrada) + "  ")

            for linha in c:
                self.idEntrada = linha[0]
                self.data_hora = linha[1]
                self.proprietario = linha[2]
                self.veiculo = linha[3]
                self.visitante = linha[4]
                self.placa = linha[5]

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca da entrada..."

    def buscarTodos(self):

        banco = BDEntrada()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from entradas order by id desc")

            todas_entradas = []
            for linha in c:

                todas_entradas.append(Entrada(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5]
                ))

            c.close()

            return todas_entradas

        except:
            return "Ocorreu um erro na busca de todas as entradas..."

    def descricao(self):
        return "Data e Hora: " + str(self.data_hora) + " | Proprietário: " + str(self.proprietario) + " | Veículo: " +\
               str(self.veiculo) + " | Visitante: " + str(self.visitante) + " | Placa: " + str(self.placa)
