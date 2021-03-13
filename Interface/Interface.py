# Autor: Bernardo Michel Slailati
# Arquivo: Interface.py
# Função: Criar interface gráfica referente a janela
# principal do software a ser desenvolvido.

# Importação das bibliotecas necessárias
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from cv2 import *
from BancoDeDados import Proprietario, Veiculo

class Interface:
    # Construtor contendo como parâmetro o objeto de interface
    # disponibilidado pela biblioteca Tkinter
    def __init__(self, master=None):
        self.master = master

        # Determinar fonte padrão a ser utilizada nos textos
        self.fontePadrao = ("Comic Sans MS", "12")

        self.tabControl = ttk.Notebook(root)
        self.tab1 = Frame(self.tabControl)
        self.tab2 = Frame(self.tabControl)
        self.tab3 = Frame(self.tabControl)
        self.tab4 = Frame(self.tabControl)

        self.criar_tab_1()
        self.criar_tab_2()
        self.criar_tab_3()
        self.criar_tab_4()

    def criar_tab_1(self):
        self.tabControl.add(self.tab1, text='Gerenciamento de Entradas')
        self.tabControl.pack(expand=1, fill="both")

        # Fragmento lateral esquerdo da janela
        self.frameLeftTab1 = Frame(self.tab1)
        self.frameLeftTab1["pady"] = 50
        self.frameLeftTab1.pack(side=LEFT)

        # Fragmento lateral direito da janela
        self.frameRightTab1 = Frame(self.tab1)
        self.frameRightTab1["padx"] = 50
        self.frameRightTab1.pack(side=RIGHT)

        # Fragmento superior da janela
        self.frameTopTab1 = Frame(self.tab1)
        self.frameTopTab1["padx"] = 50
        self.frameTopTab1.pack(side=TOP)

        # Fragmento inferior da janela
        self.frameBottomTab1 = Frame(self.tab1)
        self.frameBottomTab1["pady"] = 20
        self.frameBottomTab1.pack(fill=BOTH, expand=1, side=BOTTOM)

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL ESQUERDO
        # ---------------------------------------------------------------
        image = Image.open("icones/placa.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 4),
                                                 int(height / 4)),
                                                Image.ANTIALIAS))

        self.titulo = Label(self.frameLeftTab1, text="Placa Identificada")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.imagemPlaca = Label(self.frameLeftTab1, image=photo)
        self.imagemPlaca.image = photo
        self.imagemPlaca.pack(side=LEFT)

        self.letrasLabel = Label(self.frameLeftTab1, text="Letras:",
                                 font=self.fontePadrao)
        self.letrasLabel.pack()

        self.letras = Entry(self.frameLeftTab1)
        self.letras["width"] = 25
        self.letras["font"] = self.fontePadrao
        self.letras.pack()

        self.numerosLabel = Label(self.frameLeftTab1, text="Números:",
                                  font=self.fontePadrao)
        self.numerosLabel.pack()

        self.numeros = Entry(self.frameLeftTab1)
        self.numeros["width"] = 25
        self.numeros["font"] = self.fontePadrao
        self.numeros.pack()

        self.confirmar = Button(self.frameLeftTab1, padx=10, pady=10)
        self.confirmar["text"] = "LOCALIZAR"
        self.confirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.confirmar["width"] = 12
        self.confirmar["command"] = self.localizar_placa
        self.confirmar.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL DIREITO
        # ---------------------------------------------------------------
        self.titulo = Label(self.frameRightTab1, text="Veículo")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        image = Image.open("icones/veiculo.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 4),
                                                 int(height / 4)),
                                                Image.ANTIALIAS))

        self.imagemVeiculo = Label(self.frameRightTab1, image=photo)
        self.imagemVeiculo.image = photo
        self.imagemVeiculo.pack(side=LEFT)

        self.tipoLabel = Label(self.frameRightTab1, text="Tipo:",
                               font=self.fontePadrao)
        self.tipoLabel.pack()

        self.tipo = Entry(self.frameRightTab1)
        self.tipo["width"] = 25
        self.tipo.config(state=DISABLED)
        self.tipo["font"] = self.fontePadrao
        self.tipo.pack()

        self.corLabel = Label(self.frameRightTab1, text="Cor:",
                              font=self.fontePadrao)
        self.corLabel.pack()

        self.cor = Entry(self.frameRightTab1)
        self.cor["width"] = 25
        self.cor.config(state=DISABLED)
        self.cor["font"] = self.fontePadrao
        self.cor.pack()

        self.marcaLabel = Label(self.frameRightTab1, text="Marca:",
                                font=self.fontePadrao)
        self.marcaLabel.pack()

        self.marca = Entry(self.frameRightTab1)
        self.marca["width"] = 25
        self.marca.config(state=DISABLED)
        self.marca["font"] = self.fontePadrao
        self.marca.pack()

        self.modeloLabel = Label(self.frameRightTab1, text="Modelo:",
                                 font=self.fontePadrao)
        self.modeloLabel.pack()

        self.modelo = Entry(self.frameRightTab1)
        self.modelo["width"] = 25
        self.modelo.config(state=DISABLED)
        self.modelo["font"] = self.fontePadrao
        self.modelo.pack()

        self.anoLabel = Label(self.frameRightTab1, text="Ano:",
                              font=self.fontePadrao)
        self.anoLabel.pack()

        self.ano = Entry(self.frameRightTab1)
        self.ano["width"] = 25
        self.ano.config(state=DISABLED)
        self.ano["font"] = self.fontePadrao
        self.ano.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento SUPERIOR
        # ---------------------------------------------------------------

        image = Image.open("icones/proprietario.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 6),
                                                 int(height / 6)),
                                                Image.ANTIALIAS))

        self.titulo = Label(self.frameTopTab1, text="Proprietário/Visitante")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.imagemPessoa = Label(self.frameTopTab1, image=photo)
        self.imagemPessoa.image = photo
        self.imagemPessoa.pack(side=LEFT)

        self.nomeLabel = Label(self.frameTopTab1, text="Nome:",
                               font=self.fontePadrao)
        self.nomeLabel.pack()

        self.nome = Entry(self.frameTopTab1)
        self.nome["width"] = 25
        self.nome.config(state=DISABLED)
        self.nome["font"] = self.fontePadrao
        self.nome.pack()

        self.cpfLabel = Label(self.frameTopTab1, text="CPF:",
                              font=self.fontePadrao)
        self.cpfLabel.pack()

        self.cpf = Entry(self.frameTopTab1)
        self.cpf["width"] = 25
        self.cpf["font"] = self.fontePadrao
        self.cpf.config(state=DISABLED)
        self.cpf.pack()

        self.telefoneLabel = Label(self.frameTopTab1, text="Telefone:",
                                   font=self.fontePadrao)
        self.telefoneLabel.pack()

        self.telefone = Entry(self.frameTopTab1)
        self.telefone["width"] = 25
        self.telefone.config(state=DISABLED)
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack()

        self.apartamentoLabel = Label(self.frameTopTab1,
                                      text="Apartamento:", font=self.fontePadrao)
        self.apartamentoLabel.pack()

        self.apartamento = Entry(self.frameTopTab1)
        self.apartamento["width"] = 25
        self.apartamento.config(state=DISABLED)
        self.apartamento["font"] = self.fontePadrao
        self.apartamento.pack()

        self.visitanteLabel = Label(self.frameTopTab1, text="Visitante:",
                                    font=self.fontePadrao)
        self.visitanteLabel.pack()

        self.visitante = IntVar()

        self.simVisitante = Radiobutton(self.frameTopTab1, text="NÃO",
                                        variable=self.visitante, value=0)
        self.simVisitante["width"] = 25
        self.simVisitante["font"] = self.fontePadrao
        self.simVisitante.pack()

        self.naoVisitante = Radiobutton(self.frameTopTab1, text="SIM",
                                        variable=self.visitante, value=1)
        self.naoVisitante["width"] = 25
        self.naoVisitante["font"] = self.fontePadrao
        self.naoVisitante.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento INFERIOR
        # ---------------------------------------------------------------
        self.titulo = Label(self.frameBottomTab1, text="Últimos registros:")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.quadroRegistros = ttk.Treeview(self.frameBottomTab1,
                                            columns=("Data e Hora",
                                                     "Proprietário",
                                                     "Veículo", "Visitante",
                                                     "Placa"))
        self.quadroRegistros.heading('#0', text='Data e Hora', anchor=CENTER)
        self.quadroRegistros.heading('#1', text='Proprietário', anchor=CENTER)
        self.quadroRegistros.heading('#2', text='Veículo', anchor=CENTER)
        self.quadroRegistros.heading('#3', text='Visitante', anchor=CENTER)
        self.quadroRegistros.heading('#4', text='Placa', anchor=CENTER)

        self.quadroRegistros.column('#0', stretch=YES, width=100, anchor=CENTER)
        self.quadroRegistros.column('#1', stretch=YES, width=100, anchor=CENTER)
        self.quadroRegistros.column('#2', stretch=YES, width=100, anchor=CENTER)
        self.quadroRegistros.column('#3', stretch=YES, width=100, anchor=CENTER)
        self.quadroRegistros.column('#4', stretch=YES, width=100, anchor=CENTER)

        self.quadroRegistros.insert('', 'end', text="19-10-20 22:14",
                                    values=("Bernardo M Slailati", "Ford Ka", "NÃO", "ABC-123"))
        self.i = 0
        self.quadroRegistros.pack()

    def criar_tab_2(self):
        self.tabControl.add(self.tab2, text='Cadastro Proprietários e Veículos')

        # Fragmento superior da janela
        self.frameLeftTab2 = Frame(self.tab2)
        self.frameLeftTab2["padx"] = 50
        self.frameLeftTab2.pack(side=LEFT)

        # Fragmento lateral direito da janela
        self.frameRightTab2 = Frame(self.tab2)
        self.frameRightTab2["padx"] = 50
        self.frameRightTab2.pack(side=RIGHT)

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL ESQUERDO
        # ---------------------------------------------------------------
        image = Image.open("icones/proprietario.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 6),
                                                 int(height / 6)),
                                                Image.ANTIALIAS))

        self.cadastroProprietarioTitulo = Label(self.frameLeftTab2, text="Proprietário/Visitante")
        self.cadastroProprietarioTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.cadastroProprietarioTitulo.pack()

        self.cadastroProprietarioImagemPessoa = Label(self.frameLeftTab2, image=photo)
        self.cadastroProprietarioImagemPessoa.image = photo
        self.cadastroProprietarioImagemPessoa.pack(side=LEFT)

        self.cadastroProprietarioNomeLabel = Label(self.frameLeftTab2, text="Nome:",
                                                   font=self.fontePadrao)
        self.cadastroProprietarioNomeLabel.pack()

        self.cadastroProprietarioNome = Entry(self.frameLeftTab2)
        self.cadastroProprietarioNome["width"] = 25
        self.cadastroProprietarioNome["font"] = self.fontePadrao
        self.cadastroProprietarioNome.pack()

        self.cadastroProprietarioCpfLabel = Label(self.frameLeftTab2, text="CPF:",
                                                  font=self.fontePadrao)
        self.cadastroProprietarioCpfLabel.pack()

        self.cadastroProprietarioCpfLabel = Entry(self.frameLeftTab2)
        self.cadastroProprietarioCpfLabel["width"] = 25
        self.cadastroProprietarioCpfLabel["font"] = self.fontePadrao
        self.cadastroProprietarioCpfLabel.pack()

        self.cadastroProprietarioTelefoneLabel = Label(self.frameLeftTab2, text="Telefone:",
                                                       font=self.fontePadrao)
        self.cadastroProprietarioTelefoneLabel.pack()

        self.cadastroProprietarioTelefone = Entry(self.frameLeftTab2)
        self.cadastroProprietarioTelefone["width"] = 25
        self.cadastroProprietarioTelefone["font"] = self.fontePadrao
        self.cadastroProprietarioTelefone.pack()

        self.cadastroProprietarioApartamentoLabel = Label(self.frameLeftTab2,
                                                          text="Apartamento:", font=self.fontePadrao)
        self.cadastroProprietarioApartamentoLabel.pack()

        self.cadastroProprietarioApartamento = Entry(self.frameLeftTab2)
        self.cadastroProprietarioApartamento["width"] = 25
        self.cadastroProprietarioApartamento["font"] = self.fontePadrao
        self.cadastroProprietarioApartamento.pack()

        self.cadastroProprietarioVisitanteLabel = Label(self.frameLeftTab2, text="Visitante:",
                                                        font=self.fontePadrao)
        self.cadastroProprietarioVisitanteLabel.pack()

        self.cadastroProprietarioVisitante = IntVar()

        self.cadastroProprietarioSimVisitante = Radiobutton(self.frameLeftTab2, text="NÃO",
                                                            variable=self.cadastroProprietarioVisitante, value=0)
        self.cadastroProprietarioSimVisitante["width"] = 25
        self.cadastroProprietarioSimVisitante["font"] = self.fontePadrao
        self.cadastroProprietarioSimVisitante.pack()

        self.cadastroProprietarioNaoVisitante = Radiobutton(self.frameLeftTab2, text="SIM",
                                                            variable=self.cadastroProprietarioVisitante, value=1)
        self.cadastroProprietarioNaoVisitante["width"] = 25
        self.cadastroProprietarioNaoVisitante["font"] = self.fontePadrao
        self.cadastroProprietarioNaoVisitante.pack()

        self.cadastroProprietarioConfirmar = Button(self.frameLeftTab2, padx=10, pady=10, bg='green', fg='white')
        self.cadastroProprietarioConfirmar["text"] = "CADASTRAR PROPRIETÁRIO"
        self.cadastroProprietarioConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.cadastroProprietarioConfirmar["width"] = 24
        self.cadastroProprietarioConfirmar["command"] = self.cadastrar_proprietario
        self.cadastroProprietarioConfirmar.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL DIREITO
        # ---------------------------------------------------------------
        self.cadastroVeiculoTitulo = Label(self.frameRightTab2, text="Veículo")
        self.cadastroVeiculoTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.cadastroVeiculoTitulo.pack()

        image = Image.open("icones/veiculo.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 4),
                                                 int(height / 4)),
                                                Image.ANTIALIAS))

        self.cadastroVeiculoImagemVeiculo = Label(self.frameRightTab2, image=photo)
        self.cadastroVeiculoImagemVeiculo.image = photo
        self.cadastroVeiculoImagemVeiculo.pack(side=LEFT)

        self.cadastroVeiculoTipoLabel = Label(self.frameRightTab2, text="Tipo:",
                                              font=self.fontePadrao)
        self.cadastroVeiculoTipoLabel.pack()

        tipos_veiculo = [
            "Carro",
            "Moto",
            "Caminhonete",
            "Caminhão",
            "Ônibus",
        ]
        self.tipo_veiculo = StringVar()
        self.tipo_veiculo.set(tipos_veiculo[0])

        self.cadastroVeiculoTipo = OptionMenu(self.frameRightTab2, self.tipo_veiculo, tipos_veiculo[0],
                                              tipos_veiculo[1], tipos_veiculo[2], tipos_veiculo[3], tipos_veiculo[4])
        self.cadastroVeiculoTipo["width"] = 25
        self.cadastroVeiculoTipo["font"] = self.fontePadrao
        self.cadastroVeiculoTipo["menu"].config(bg="white")
        self.cadastroVeiculoTipo.pack()

        self.cadastroVeiculoCorLabel = Label(self.frameRightTab2, text="Cor:",
                                             font=self.fontePadrao)
        self.cadastroVeiculoCorLabel.pack()

        self.cadastroVeiculoCor = Entry(self.frameRightTab2)
        self.cadastroVeiculoCor["width"] = 25
        self.cadastroVeiculoCor["font"] = self.fontePadrao
        self.cadastroVeiculoCor.pack()

        self.cadastroVeiculoMarcaLabel = Label(self.frameRightTab2, text="Marca:",
                                               font=self.fontePadrao)
        self.cadastroVeiculoMarcaLabel.pack()

        self.cadastroVeiculoMarca = Entry(self.frameRightTab2)
        self.cadastroVeiculoMarca["width"] = 25
        self.cadastroVeiculoMarca["font"] = self.fontePadrao
        self.cadastroVeiculoMarca.pack()

        self.cadastroVeiculoModeloLabel = Label(self.frameRightTab2, text="Modelo:",
                                                font=self.fontePadrao)
        self.cadastroVeiculoModeloLabel.pack()

        self.cadastroVeiculoModelo = Entry(self.frameRightTab2)
        self.cadastroVeiculoModelo["width"] = 25
        self.cadastroVeiculoModelo["font"] = self.fontePadrao
        self.cadastroVeiculoModelo.pack()

        self.cadastroVeiculoAnoLabel = Label(self.frameRightTab2, text="Ano:",
                                             font=self.fontePadrao)
        self.cadastroVeiculoAnoLabel.pack()

        self.cadastroVeiculoAno = Entry(self.frameRightTab2)
        self.cadastroVeiculoAno["width"] = 25
        self.cadastroVeiculoAno["font"] = self.fontePadrao
        self.cadastroVeiculoAno.pack()

        self.cadastroProprietarioConfirmar = Button(self.frameRightTab2, padx=10, pady=10, bg='green', fg='white')
        self.cadastroProprietarioConfirmar["text"] = "CADASTRAR VEÍCULO"
        self.cadastroProprietarioConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.cadastroProprietarioConfirmar["width"] = 24
        self.cadastroProprietarioConfirmar["command"] = self.cadastrar_veiculo
        self.cadastroProprietarioConfirmar.pack()

    def criar_tab_3(self):
        self.tabControl.add(self.tab3, text='Modificar/Remover Proprietários e Veículos')

    def criar_tab_4(self):
        self.tabControl.add(self.tab4, text='Registro de Entradas')

    # Inserir proprietário
    def cadastrar_proprietario(self):
        proprietario = Proprietario.Proprietario(
            0,
            str(self.cadastroProprietarioNome.get()),
            str(self.cadastroProprietarioTelefone.get()),
            str(self.cadastroProprietarioApartamento.get()),
            str(self.cadastroProprietarioVisitante.get())
        )

        resposta = proprietario.inserir()
        print(resposta)
        if "sucesso" in resposta:
            messagebox.showinfo("Sucesso", resposta)
        else:
            messagebox.showerror("Erro", resposta)

        print(proprietario.descricao())

    # Inserir veiculo
    def cadastrar_veiculo(self):
        veiculo = Veiculo.Veiculo(
            0,
            str(self.tipo_veiculo.get()),
            str(self.cadastroVeiculoCor.get()),
            str(self.cadastroVeiculoMarca.get()),
            str(self.cadastroVeiculoModelo.get()),
            str(self.cadastroVeiculoAno.get()),
            str(self.cadastroVeiculoAno.get())
        )

        resposta = "Ocorreu um erro na inserção do veículo..."
        print(resposta)
        if "sucesso" in resposta:
            messagebox.showinfo("Sucesso", resposta)
        else:
            messagebox.showerror("Erro", resposta)

        print(veiculo.descricao())


    # Função a ser criada, iniciada após o clique do botão 'Localizar'
    def localizar_placa(self):
        self.cpf.config(state=NORMAL)
        self.cpf.delete(0, END)
        self.cpf.insert(0, "07253441648")
        self.cpf.config(state=DISABLED)


# Inicialização da interface gráfica principal da janela desenvolvida
# para o sistema
root = Tk()
root.title("Controle de Acesso Veicular Condominial")
imgicon = PhotoImage(file=os.path.join('icones/logo.png'))
root.tk.call('wm', 'iconphoto', root.w, imgicon)
Interface(root)
root.mainloop()