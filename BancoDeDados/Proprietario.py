from BancoDeDados.BDProprietario import BDProprietario


class Proprietario:

    def __init__(self, idproprietario=0, nome="", telefone="", apartamento="", visitante=""):
        self.info = {}
        self.idproprietario = idproprietario
        self.nome = nome
        self.telefone = telefone
        self.apartamento = apartamento
        self.visitante = visitante

    def inserir(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into proprietarios (nome, telefone, apartamento, visitante) values ('" + self.nome + "', '" +
                self.telefone + "', '" + self.apartamento + "', '" + str(self.visitante) + "' )")

            banco.conexao.commit()
            c.close()

            return "Proprietário cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do proprietário..."

    def atualizar(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', apartamento = '" +
                self.apartamento + "', visitante = '" + self.visitante + "' where idproprietario = " +
                str(self.idproprietario) + " ")

            banco.conexao.commit()
            c.close()

            return "Proprietário atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do proprietário..."

    def deletar(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("delete from proprietarios where idproprietario = " + str(self.idproprietario) + " ")

            banco.conexao.commit()
            c.close()

            return "Proprietário excluído com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do proprietário..."

    def buscar(self, idproprietario):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from proprietarios where idproprietario = " + idproprietario + "  ")

            for linha in c:
                self.idproprietario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.apartamento = linha[3]
                self.visitante = linha[4]

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do proprietário..."

    def descricao(self):
        return "Nome: " + str(self.nome) + " | " + str(self.telefone) + " | Ap: " + str(self.apartamento) + " | Visitante? " \
               + str(self.visitante)