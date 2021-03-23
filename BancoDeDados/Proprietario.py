from BancoDeDados.BDProprietario import BDProprietario


class Proprietario:

    def __init__(self, idproprietario=0, nome="", cpf="", telefone="", apartamento="", visitante=""):
        self.info = {}
        self.idproprietario = idproprietario
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.apartamento = apartamento
        self.visitante = visitante

    def inserir(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            visitante_sim_nao = "DESCONHECIDO"

            if str(self.visitante) == "0":
                visitante_sim_nao = "NÃO"
            elif str(self.visitante) == "1":
                visitante_sim_nao = "SIM"

            c.execute(
                "insert into proprietarios (nome, cpf, telefone, apartamento, visitante) values ('" + self.nome +
                "', '" + self.cpf + "', '" + self.telefone + "', '" + self.apartamento + "', '" +
                visitante_sim_nao + "' )")

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
                "update proprietarios set nome = '" + self.nome + "', cpf = '" + self.cpf + "', telefone = '" +
                self.telefone + "', apartamento = '" + self.apartamento + "', visitante = '" + self.visitante +
                "' where id = " + str(self.idproprietario) + " ")

            banco.conexao.commit()
            c.close()

            return "Proprietário atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do proprietário..."

    def deletar(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("delete from proprietarios where id = " + str(self.idproprietario))

            banco.conexao.commit()
            c.close()

            return "Proprietário excluído com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do proprietário..."

    def buscar(self, idproprietario):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from proprietarios where id = " + str(idproprietario) + "  ")

            for linha in c:
                self.idproprietario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.apartamento = linha[4]
                self.visitante = linha[5]

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do proprietário..."

    def pesquisar(self, tipoPesquisa, valorPesquisa):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from proprietarios where lower(" + str(tipoPesquisa).lower() + ") = '" +
                               str(valorPesquisa).lower() + "' order by id limit 1")

            for linha in c:
                self.idproprietario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.apartamento = linha[4]
                self.visitante = linha[5]

            c.close()

            return self

        except:
            return None

    def buscarTodosCpfs(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("select cpf from proprietarios order by cpf")

            todos_cpfs = []
            for linha in c:
                todos_cpfs.append(linha[0])

            c.close()

            return todos_cpfs

        except:
            return "Ocorreu um erro na busca de todos os CPFs de proprietários..."

    def buscarTodos(self):

        banco = BDProprietario()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from proprietarios order by id")

            todos_proprietarios = []
            for linha in c:

                todos_proprietarios.append(Proprietario(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5]
                ))

            c.close()

            return todos_proprietarios

        except:
            return "Ocorreu um erro na busca de todos os proprietários..."

    def descricao(self):
        return "Nome: " + self.nome + " | CPF: " + self.cpf + " | Telefone: " + self.telefone + " | Ap: " + \
               self.apartamento + " | Visitante? " + str(self.visitante)
