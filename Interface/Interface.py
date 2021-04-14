# Autor: Bernardo Michel Slailati
# Arquivo: Interface.py
# Função: Criar interface gráfica referente a janela
# principal do software a ser desenvolvido.

# Importação das bibliotecas necessárias
import glob

from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from BancoDeDados import Proprietario, Veiculo, Entrada
from cv2 import *
from IdentificacaoPlacas import IdentificaPlaca
from IdentificacaoCaracteres import IdentificaCaracteres
import pytesseract as pytess

pytess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

DEBUG = True


class Interface:
    # Construtor contendo como parâmetro o objeto de interface
    # disponibilizado pela biblioteca Tkinter
    def __init__(self, master=None):
        self.master = master

        self.proprietario_modificar = None
        self.veiculo_modificar = None
        self.entrada_modificar = None

        # Determinar fonte padrão a ser utilizada nos textos
        self.fontePadrao = ("Comic Sans MS", "12")

        self.tabControl = ttk.Notebook(root)
        self.tab1 = Frame(self.tabControl)
        self.tab2 = Frame(self.tabControl)
        self.tab3 = Frame(self.tabControl)
        self.tab4 = Frame(self.tabControl)
        self.tab5 = Frame(self.tabControl)

        self.criar_tab_1()
        self.criar_tab_2()
        self.criar_tab_3()
        self.criar_tab_4()
        self.criar_tab_5()

        self.buscar_todos_proprietarios()
        self.buscar_todos_veiculos()
        self.buscar_todas_entradas()

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
        self.frameBottomTab1.pack(side=BOTTOM, fill="both", expand=True)

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL ESQUERDO
        # ---------------------------------------------------------------
        image = Image.open("icones/placa.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 8),
                                                 int(height / 8)),
                                                Image.ANTIALIAS))

        self.titulo = Label(self.frameLeftTab1, text="Placa Identificada")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.imagemPlaca = Label(self.frameLeftTab1, image=photo)
        self.imagemPlaca.image = photo
        self.imagemPlaca.pack()

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

        self.confirmar = Button(self.frameLeftTab1, padx=10, pady=10, bg='blue', fg='white')
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
        photo = ImageTk.PhotoImage(image.resize((int(width / 10),
                                                 int(height / 10)),
                                                Image.ANTIALIAS))

        self.imagemVeiculo = Label(self.frameRightTab1, image=photo)
        self.imagemVeiculo.image = photo
        self.imagemVeiculo.pack()

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

        self.placaLabel = Label(self.frameRightTab1, text="Placa:",
                                font=self.fontePadrao)
        self.placaLabel.pack()

        self.placa = Entry(self.frameRightTab1)
        self.placa["width"] = 25
        self.placa.config(state=DISABLED)
        self.placa["font"] = self.fontePadrao
        self.placa.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento SUPERIOR
        # ---------------------------------------------------------------

        image = Image.open("icones/proprietario.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 10),
                                                 int(height / 10)),
                                                Image.ANTIALIAS))

        self.titulo = Label(self.frameTopTab1, text="Proprietário/Visitante")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.imagemPessoa = Label(self.frameTopTab1, image=photo)
        self.imagemPessoa.image = photo
        self.imagemPessoa.pack()

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
        self.simVisitante.config(state=DISABLED)
        self.simVisitante.pack()

        self.naoVisitante = Radiobutton(self.frameTopTab1, text="SIM",
                                        variable=self.visitante, value=1)
        self.naoVisitante["width"] = 25
        self.naoVisitante["font"] = self.fontePadrao
        self.naoVisitante.config(state=DISABLED)
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

        self.quadroRegistros.column('#0', minwidth=75, width=150, stretch=NO, anchor=CENTER)
        self.quadroRegistros.column('#1', minwidth=125, width=225, stretch=NO, anchor=CENTER)
        self.quadroRegistros.column('#2', minwidth=75, width=175, stretch=NO, anchor=CENTER)
        self.quadroRegistros.column('#3', minwidth=50, width=75, stretch=NO, anchor=CENTER)
        self.quadroRegistros.column('#4', minwidth=75, width=150, stretch=NO, anchor=CENTER)

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
        photo = ImageTk.PhotoImage(image.resize((int(width / 8),
                                                 int(height / 8)),
                                                Image.ANTIALIAS))

        self.cadastroProprietarioTitulo = Label(self.frameLeftTab2, text="Proprietário/Visitante")
        self.cadastroProprietarioTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.cadastroProprietarioTitulo.pack()

        self.cadastroProprietarioImagemPessoa = Label(self.frameLeftTab2, image=photo)
        self.cadastroProprietarioImagemPessoa.image = photo
        self.cadastroProprietarioImagemPessoa.pack()

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

        self.cadastroProprietarioCpf = Entry(self.frameLeftTab2)
        self.cadastroProprietarioCpf["width"] = 25
        self.cadastroProprietarioCpf["font"] = self.fontePadrao
        self.cadastroProprietarioCpf.pack()

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
        photo = ImageTk.PhotoImage(image.resize((int(width / 8),
                                                 int(height / 8)),
                                                Image.ANTIALIAS))

        self.cadastroVeiculoImagemVeiculo = Label(self.frameRightTab2, image=photo)
        self.cadastroVeiculoImagemVeiculo.image = photo
        self.cadastroVeiculoImagemVeiculo.pack()

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

        self.cadastroVeiculoTipo = OptionMenu(self.frameRightTab2, self.tipo_veiculo, *tipos_veiculo)
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

        self.cadastroVeiculoPlacaLabel = Label(self.frameRightTab2, text="Placa:",
                                               font=self.fontePadrao)
        self.cadastroVeiculoPlacaLabel.pack()

        self.cadastroVeiculoPlaca = Entry(self.frameRightTab2)
        self.cadastroVeiculoPlaca["width"] = 25
        self.cadastroVeiculoPlaca["font"] = self.fontePadrao
        self.cadastroVeiculoPlaca.pack()

        self.cadastroVeiculoCpfProprietarioLabel = Label(self.frameRightTab2, text="CPF Proprietário:",
                                                         font=self.fontePadrao)
        self.cadastroVeiculoCpfProprietarioLabel.pack()

        cpfs_proprietarios = Proprietario.Proprietario().buscarTodosCpfs()
        self.cpf_proprietario = StringVar()

        if len(cpfs_proprietarios) > 0:
            self.cpf_proprietario.set(cpfs_proprietarios[0])

            self.cadastroVeiculoCpfProprietario = OptionMenu(self.frameRightTab2, self.cpf_proprietario,
                                                             *cpfs_proprietarios)
            self.cadastroVeiculoCpfProprietario["width"] = 25
            self.cadastroVeiculoCpfProprietario["font"] = self.fontePadrao
            self.cadastroVeiculoCpfProprietario.pack()
        else:
            self.cadastroVeiculoCpfProprietario = Label(self.frameRightTab2, text="Nenhum proprietário registrado...",
                                                        font=self.fontePadrao, padx=10, pady=10)
            self.cadastroVeiculoCpfProprietario.pack()

        self.cadastroVeiculoAtualizarCpfs = Button(self.frameRightTab2, padx=10, pady=10, bg='blue', fg='white')
        self.cadastroVeiculoAtualizarCpfs["text"] = "ATUALIZAR CPFS"
        self.cadastroVeiculoAtualizarCpfs["font"] = ("Comics Sans MS", "8", "bold")
        self.cadastroVeiculoAtualizarCpfs["width"] = 24
        self.cadastroVeiculoAtualizarCpfs["command"] = self.atualizar_cpfs
        self.cadastroVeiculoAtualizarCpfs.pack(side=RIGHT)

        self.cadastroVeiculoConfirmar = Button(self.frameRightTab2, padx=10, pady=10, bg='green', fg='white')
        self.cadastroVeiculoConfirmar["text"] = "CADASTRAR VEÍCULO"
        self.cadastroVeiculoConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.cadastroVeiculoConfirmar["width"] = 24
        self.cadastroVeiculoConfirmar["command"] = self.cadastrar_veiculo
        self.cadastroVeiculoConfirmar.pack()

    def criar_tab_3(self):
        self.tabControl.add(self.tab3, text='Modificar/Remover Proprietários e Veículos')

        # Fragmento superior da janela
        self.frameLeftTab3 = Frame(self.tab3)
        self.frameLeftTab3["padx"] = 50
        self.frameLeftTab3.pack(side=LEFT)

        # Fragmento inferior da janela
        self.frameRightTab3 = Frame(self.tab3)
        self.frameRightTab3["padx"] = 50
        self.frameRightTab3.pack(side=RIGHT)

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento ESQUERDO
        # ---------------------------------------------------------------

        image = Image.open("icones/proprietario.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 10),
                                                 int(height / 10)),
                                                Image.ANTIALIAS))

        self.alterarProprietarioTitulo = Label(self.frameLeftTab3, text="Proprietário/Visitante")
        self.alterarProprietarioTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.alterarProprietarioTitulo.pack()

        self.alterarProprietarioImagemPessoa = Label(self.frameLeftTab3, image=photo)
        self.alterarProprietarioImagemPessoa.image = photo
        self.alterarProprietarioImagemPessoa.pack()

        self.alterarProprietarioPesquisarPorLabel = Label(self.frameLeftTab3, text="Pesquisar por:",
                                                          font=self.fontePadrao)
        self.alterarProprietarioPesquisarPorLabel.pack()

        todos_pesquisar_por_proprietario = [
            "Apartamento",
            "Nome",
            "CPF",
            "ID",
        ]

        self.pequisar_por_proprietario = StringVar()
        self.pequisar_por_proprietario.set(todos_pesquisar_por_proprietario[0])

        self.alterarProprietarioPesquisarPor = OptionMenu(self.frameLeftTab3, self.pequisar_por_proprietario,
                                                          *todos_pesquisar_por_proprietario)
        self.alterarProprietarioPesquisarPor["width"] = 25
        self.alterarProprietarioPesquisarPor["font"] = self.fontePadrao
        self.alterarProprietarioPesquisarPor["menu"].config(bg="white")
        self.alterarProprietarioPesquisarPor.pack()

        self.alterarProprietarioPesquisar = Entry(self.frameLeftTab3, bg="#DDDDDD")
        self.alterarProprietarioPesquisar["width"] = 25
        self.alterarProprietarioPesquisar["font"] = self.fontePadrao
        self.alterarProprietarioPesquisar.insert(0, "Pesquisar...")
        self.alterarProprietarioPesquisar.pack()

        self.alterarProprietarioPesquisarConfirmar = Button(self.frameLeftTab3, padx=10, pady=10, bg='blue', fg='white')
        self.alterarProprietarioPesquisarConfirmar["text"] = "PESQUISAR"
        self.alterarProprietarioPesquisarConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.alterarProprietarioPesquisarConfirmar["width"] = 24
        self.alterarProprietarioPesquisarConfirmar["command"] = self.pesquisar_proprietario
        self.alterarProprietarioPesquisarConfirmar.pack(pady=5)

        self.alterarProprietarioNomeLabel = Label(self.frameLeftTab3, text="Nome:",
                                                  font=self.fontePadrao)
        self.alterarProprietarioNomeLabel.pack()

        self.alterarProprietarioNome = Entry(self.frameLeftTab3)
        self.alterarProprietarioNome["width"] = 25
        self.alterarProprietarioNome["font"] = self.fontePadrao
        self.alterarProprietarioNome.pack()

        self.alterarProprietarioCpfLabel = Label(self.frameLeftTab3, text="CPF:",
                                                 font=self.fontePadrao)
        self.alterarProprietarioCpfLabel.pack()

        self.alterarProprietarioCpf = Entry(self.frameLeftTab3)
        self.alterarProprietarioCpf["width"] = 25
        self.alterarProprietarioCpf["font"] = self.fontePadrao
        self.alterarProprietarioCpf.pack()

        self.alterarProprietarioTelefoneLabel = Label(self.frameLeftTab3, text="Telefone:",
                                                      font=self.fontePadrao)
        self.alterarProprietarioTelefoneLabel.pack()

        self.alterarProprietarioTelefone = Entry(self.frameLeftTab3)
        self.alterarProprietarioTelefone["width"] = 25
        self.alterarProprietarioTelefone["font"] = self.fontePadrao
        self.alterarProprietarioTelefone.pack()

        self.alterarProprietarioApartamentoLabel = Label(self.frameLeftTab3,
                                                         text="Apartamento:", font=self.fontePadrao)
        self.alterarProprietarioApartamentoLabel.pack()

        self.alterarProprietarioApartamento = Entry(self.frameLeftTab3)
        self.alterarProprietarioApartamento["width"] = 25
        self.alterarProprietarioApartamento["font"] = self.fontePadrao
        self.alterarProprietarioApartamento.pack()

        self.alterarProprietarioVisitanteLabel = Label(self.frameLeftTab3, text="Visitante:",
                                                       font=self.fontePadrao)
        self.alterarProprietarioVisitanteLabel.pack()

        self.alterarProprietarioVisitante = Entry(self.frameLeftTab3)
        self.alterarProprietarioVisitante["width"] = 25
        self.alterarProprietarioVisitante["font"] = self.fontePadrao
        self.alterarProprietarioVisitante.pack(padx=10, pady=10)

        self.alterarProprietarioConfirmar = Button(self.frameLeftTab3, padx=10, pady=10, bg='green', fg='white')
        self.alterarProprietarioConfirmar["text"] = "ALTERAR PROPRIETÁRIO"
        self.alterarProprietarioConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.alterarProprietarioConfirmar["width"] = 24
        self.alterarProprietarioConfirmar["command"] = self.alterar_proprietario
        self.alterarProprietarioConfirmar.pack(side=LEFT)

        self.alterarProprietarioDeletar = Button(self.frameLeftTab3, padx=10, pady=10, bg='red', fg='white')
        self.alterarProprietarioDeletar["text"] = "DELETAR PROPRIETÁRIO"
        self.alterarProprietarioDeletar["font"] = ("Comics Sans MS", "8", "bold")
        self.alterarProprietarioDeletar["width"] = 24
        self.alterarProprietarioDeletar["command"] = self.deletar_proprietario
        self.alterarProprietarioDeletar.pack(side=RIGHT)

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento DIREITO
        # ---------------------------------------------------------------

        image = Image.open("icones/veiculo.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 10),
                                                 int(height / 10)),
                                                Image.ANTIALIAS))

        self.alterarVeiculoTitulo = Label(self.frameRightTab3, text="Veículo")
        self.alterarVeiculoTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.alterarVeiculoTitulo.pack()

        self.alterarVeiculoImagemVeiculo = Label(self.frameRightTab3, image=photo)
        self.alterarVeiculoImagemVeiculo.image = photo
        self.alterarVeiculoImagemVeiculo.pack()

        self.alterarVeiculoPesquisarPorLabel = Label(self.frameRightTab3, text="Pesquisar por:",
                                                     font=self.fontePadrao)
        self.alterarVeiculoPesquisarPorLabel.pack()

        todos_pesquisar_por_veiculo = [
            "Placa",
            "CPF Proprietário",
            "ID"
        ]

        self.pesquisar_por_veiculo = StringVar()
        self.pesquisar_por_veiculo.set(todos_pesquisar_por_veiculo[0])

        self.alterarVeiculoPesquisarPor = OptionMenu(self.frameRightTab3, self.pesquisar_por_veiculo,
                                                     *todos_pesquisar_por_veiculo)
        self.alterarVeiculoPesquisarPor["width"] = 25
        self.alterarVeiculoPesquisarPor["font"] = self.fontePadrao
        self.alterarVeiculoPesquisarPor["menu"].config(bg="white")
        self.alterarVeiculoPesquisarPor.pack()

        self.alterarVeiculoPesquisar = Entry(self.frameRightTab3, bg="#DDDDDD")
        self.alterarVeiculoPesquisar["width"] = 25
        self.alterarVeiculoPesquisar["font"] = self.fontePadrao
        self.alterarVeiculoPesquisar.insert(0, "Pesquisar...")
        self.alterarVeiculoPesquisar.pack()

        self.alterarVeiculoPesquisarConfirmar = Button(self.frameRightTab3, padx=10, pady=10, bg='blue', fg='white')
        self.alterarVeiculoPesquisarConfirmar["text"] = "PESQUISAR"
        self.alterarVeiculoPesquisarConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.alterarVeiculoPesquisarConfirmar["width"] = 24
        self.alterarVeiculoPesquisarConfirmar["command"] = self.pesquisar_veiculo
        self.alterarVeiculoPesquisarConfirmar.pack(pady=5)

        self.alterarVeiculoTipoLabel = Label(self.frameRightTab3, text="Tipo:",
                                             font=self.fontePadrao)
        self.alterarVeiculoTipoLabel.pack()

        self.alterarVeiculoTipo = Entry(self.frameRightTab3)
        self.alterarVeiculoTipo["width"] = 25
        self.alterarVeiculoTipo["font"] = self.fontePadrao
        self.alterarVeiculoTipo.pack()

        self.alterarVeiculoCorLabel = Label(self.frameRightTab3, text="Cor:",
                                            font=self.fontePadrao)
        self.alterarVeiculoCorLabel.pack()

        self.alterarVeiculoCor = Entry(self.frameRightTab3)
        self.alterarVeiculoCor["width"] = 25
        self.alterarVeiculoCor["font"] = self.fontePadrao
        self.alterarVeiculoCor.pack()

        self.alterarVeiculoMarcaLabel = Label(self.frameRightTab3, text="Marca:",
                                              font=self.fontePadrao)
        self.alterarVeiculoMarcaLabel.pack()

        self.alterarVeiculoMarca = Entry(self.frameRightTab3)
        self.alterarVeiculoMarca["width"] = 25
        self.alterarVeiculoMarca["font"] = self.fontePadrao
        self.alterarVeiculoMarca.pack()

        self.alterarVeiculoModeloLabel = Label(self.frameRightTab3, text="Modelo:",
                                               font=self.fontePadrao)
        self.alterarVeiculoModeloLabel.pack()

        self.alterarVeiculoModelo = Entry(self.frameRightTab3)
        self.alterarVeiculoModelo["width"] = 25
        self.alterarVeiculoModelo["font"] = self.fontePadrao
        self.alterarVeiculoModelo.pack()

        self.alterarVeiculoAnoLabel = Label(self.frameRightTab3, text="Ano:",
                                            font=self.fontePadrao)
        self.alterarVeiculoAnoLabel.pack()

        self.alterarVeiculoAno = Entry(self.frameRightTab3)
        self.alterarVeiculoAno["width"] = 25
        self.alterarVeiculoAno["font"] = self.fontePadrao
        self.alterarVeiculoAno.pack()

        self.alterarVeiculoPlacaLabel = Label(self.frameRightTab3, text="Placa:",
                                              font=self.fontePadrao)
        self.alterarVeiculoPlacaLabel.pack()

        self.alterarVeiculoPlaca = Entry(self.frameRightTab3)
        self.alterarVeiculoPlaca["width"] = 25
        self.alterarVeiculoPlaca["font"] = self.fontePadrao
        self.alterarVeiculoPlaca.pack()

        self.alterarVeiculoCpfProprietarioLabel = Label(self.frameRightTab3, text="CPF Proprietário:",
                                                        font=self.fontePadrao)
        self.alterarVeiculoCpfProprietarioLabel.pack()

        self.alterarVeiculoCpfProprietario = Entry(self.frameRightTab3)
        self.alterarVeiculoCpfProprietario["width"] = 25
        self.alterarVeiculoCpfProprietario["font"] = self.fontePadrao
        self.alterarVeiculoCpfProprietario.config(state=DISABLED)
        self.alterarVeiculoCpfProprietario.pack(padx=10, pady=10)

        self.alterarVeiculoConfirmar = Button(self.frameRightTab3, padx=10, pady=10, bg='green', fg='white')
        self.alterarVeiculoConfirmar["text"] = "ALTERAR VEÍCULO"
        self.alterarVeiculoConfirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.alterarVeiculoConfirmar["width"] = 24
        self.alterarVeiculoConfirmar["command"] = self.alterar_veiculo
        self.alterarVeiculoConfirmar.pack(side=LEFT)

        self.alterarVeiculoDeletar = Button(self.frameRightTab3, padx=10, pady=10, bg='red', fg='white')
        self.alterarVeiculoDeletar["text"] = "DELETAR PROPRIETÁRIO"
        self.alterarVeiculoDeletar["font"] = ("Comics Sans MS", "8", "bold")
        self.alterarVeiculoDeletar["width"] = 24
        self.alterarVeiculoDeletar["command"] = self.deletar_veiculo
        self.alterarVeiculoDeletar.pack(side=RIGHT)

    def criar_tab_4(self):
        self.tabControl.add(self.tab4, text='Registro de Entradas')

        # Fragmento lateral superior da janela
        self.frameTopTab4 = Frame(self.tab4)
        self.frameTopTab4["pady"] = 50
        self.frameTopTab4.pack(side=TOP)

        self.registrosTitulo = Label(self.frameTopTab4, text="Registro Geral de Entradas")
        self.registrosTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.registrosTitulo.pack()

        self.registrosQuadroRegistros = ttk.Treeview(self.frameTopTab4,
                                                     columns=("ID",
                                                              "Data e Hora",
                                                              "Proprietário",
                                                              "Veículo", "Visitante",
                                                              "Placa"))
        self.registrosQuadroRegistros.heading('#0', text='ID', anchor=CENTER)
        self.registrosQuadroRegistros.heading('#1', text='Data e Hora', anchor=CENTER)
        self.registrosQuadroRegistros.heading('#2', text='Proprietário', anchor=CENTER)
        self.registrosQuadroRegistros.heading('#3', text='Veículo', anchor=CENTER)
        self.registrosQuadroRegistros.heading('#4', text='Visitante', anchor=CENTER)
        self.registrosQuadroRegistros.heading('#5', text='Placa', anchor=CENTER)

        self.registrosQuadroRegistros.column('#0', minwidth=20, width=50, stretch=NO, anchor=CENTER)
        self.registrosQuadroRegistros.column('#1', minwidth=120, width=150, stretch=NO, anchor=CENTER)
        self.registrosQuadroRegistros.column('#2', minwidth=175, width=275, stretch=NO, anchor=CENTER)
        self.registrosQuadroRegistros.column('#3', minwidth=175, width=275, stretch=NO, anchor=CENTER)
        self.registrosQuadroRegistros.column('#4', minwidth=75, width=100, stretch=NO, anchor=CENTER)
        self.registrosQuadroRegistros.column('#5', minwidth=75, width=100, stretch=NO, anchor=CENTER)

        self.registrosQuadroRegistros.bind("<Delete>", self.deletar_entrada)

        self.registrosQuadroRegistros.pack()

        self.registrosAtualizar = Button(self.frameTopTab4, padx=10, pady=10, bg='blue', fg='white')
        self.registrosAtualizar["text"] = "ATUALIZAR"
        self.registrosAtualizar["font"] = ("Comics Sans MS", "8", "bold")
        self.registrosAtualizar["width"] = 24
        self.registrosAtualizar["command"] = self.buscar_todas_entradas
        self.registrosAtualizar.pack()

    def criar_tab_5(self):
        self.tabControl.add(self.tab5, text='Registro de Proprietários e Veículos')

        # Fragmento superior da janela
        self.frameTopTab5 = Frame(self.tab5)
        self.frameTopTab5["padx"] = 50
        self.frameTopTab5.pack(side=TOP)

        # Fragmento inferior da janela
        self.frameBottomTab5 = Frame(self.tab5)
        self.frameBottomTab5["padx"] = 50
        self.frameBottomTab5.pack(side=BOTTOM)

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento SUPERIOR
        # ---------------------------------------------------------------
        self.proprietariosTitulo = Label(self.frameTopTab5, text="Registro Geral de Proprietários")
        self.proprietariosTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.proprietariosTitulo.pack()

        self.proprietariosQuadroRegistros = ttk.Treeview(self.frameTopTab5,
                                                         columns=("ID",
                                                                  "Nome",
                                                                  "CPF", "Telefone",
                                                                  "Apartamento", "Visitante"))
        self.proprietariosQuadroRegistros.heading('#0', text='ID', anchor=CENTER)
        self.proprietariosQuadroRegistros.heading('#1', text='Nome', anchor=CENTER)
        self.proprietariosQuadroRegistros.heading('#2', text='CPF', anchor=CENTER)
        self.proprietariosQuadroRegistros.heading('#3', text='Telefone', anchor=CENTER)
        self.proprietariosQuadroRegistros.heading('#4', text='Apartamento', anchor=CENTER)
        self.proprietariosQuadroRegistros.heading('#5', text='Visitante', anchor=CENTER)

        self.proprietariosQuadroRegistros.column('#0', minwidth=20, width=50, stretch=NO, anchor=CENTER)
        self.proprietariosQuadroRegistros.column('#1', minwidth=175, width=275, stretch=NO, anchor=CENTER)
        self.proprietariosQuadroRegistros.column('#2', minwidth=120, width=150, stretch=NO, anchor=CENTER)
        self.proprietariosQuadroRegistros.column('#3', minwidth=75, width=120, stretch=NO, anchor=CENTER)
        self.proprietariosQuadroRegistros.column('#4', minwidth=75, width=120, stretch=NO, anchor=CENTER)
        self.proprietariosQuadroRegistros.column('#5', minwidth=75, width=120, stretch=NO, anchor=CENTER)

        self.proprietariosQuadroRegistros.pack()

        self.proprietariosAtualizar = Button(self.frameTopTab5, padx=10, pady=10, bg='blue', fg='white')
        self.proprietariosAtualizar["text"] = "ATUALIZAR"
        self.proprietariosAtualizar["font"] = ("Comics Sans MS", "8", "bold")
        self.proprietariosAtualizar["width"] = 24
        self.proprietariosAtualizar["command"] = self.buscar_todos_proprietarios
        self.proprietariosAtualizar.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento INFERIOR
        # ---------------------------------------------------------------
        self.veiculosTitulo = Label(self.frameBottomTab5, text="Registro Geral de Veículos")
        self.veiculosTitulo["font"] = ("Comic Sans MS", "14", "bold")
        self.veiculosTitulo.pack()

        self.veiculosQuadroRegistros = ttk.Treeview(self.frameBottomTab5, columns=['ID', 'Tipo', 'Marca', 'Modelo',
                                                                                   'Ano', 'Cor', 'Placa',
                                                                                   'CPF Proprietário'])

        self.veiculosQuadroRegistros.heading('#0', text='ID', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#1', text='Tipo', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#2', text='Marca', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#3', text='Modelo', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#4', text='Ano', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#5', text='Cor', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#6', text='Placa', anchor=CENTER)
        self.veiculosQuadroRegistros.heading('#7', text='CPF Proprietário', anchor=CENTER)

        self.veiculosQuadroRegistros.column('#0', minwidth=20, width=50, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#1', minwidth=75, width=120, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#2', minwidth=150, width=220, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#3', minwidth=150, width=220, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#4', minwidth=75, width=120, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#5', minwidth=75, width=120, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#6', minwidth=75, width=120, stretch=NO, anchor=CENTER)
        self.veiculosQuadroRegistros.column('#7', minwidth=150, width=220, stretch=NO, anchor=CENTER)

        self.veiculosQuadroRegistros.pack()

        self.veiculosAtualizar = Button(self.frameBottomTab5, padx=10, pady=10, bg='blue', fg='white')
        self.veiculosAtualizar["text"] = "ATUALIZAR"
        self.veiculosAtualizar["font"] = ("Comics Sans MS", "8", "bold")
        self.veiculosAtualizar["width"] = 24
        self.veiculosAtualizar["command"] = self.buscar_todos_veiculos
        self.veiculosAtualizar.pack()

    def deletar_entrada(self, event=None):
        global linha

        try:
            if len(self.registrosQuadroRegistros.selection()) != 0:
                linha = self.registrosQuadroRegistros.selection()
                entrada = self.registrosQuadroRegistros.item(linha)

                resposta = messagebox.askyesno("Deletar Entrada",
                                               "Deseja realmente deletar essa entrada? Ao ser excluída nunca mais "
                                               "poderá ser recuperada.")
                if resposta:
                    idEntrada = entrada["text"]
                    resposta = Entrada.Entrada().deletar(idEntrada)

                    if "sucesso" in resposta:
                        messagebox.showinfo("Sucesso", resposta)
                        self.buscar_todas_entradas()
                    else:
                        messagebox.showerror("Falha ao deletar", resposta)

                else:
                    messagebox.showerror("Cancelado", "Cancelada exclusão de entrada!")
        except:
            messagebox.showwarning("Necessário escolher uma entrada", "Escolha uma entrada a ser deletada.")

    # Buscar todos proprietários
    def buscar_todos_proprietarios(self):
        proprietario = Proprietario.Proprietario()

        resposta = proprietario.buscarTodos()

        self.proprietariosQuadroRegistros.delete(*self.proprietariosQuadroRegistros.get_children())
        for proprietario in resposta:
            self.proprietariosQuadroRegistros.insert('', END, text=str(proprietario.idproprietario),
                                                     values=(
                                                         proprietario.nome,
                                                         proprietario.cpf,
                                                         proprietario.telefone,
                                                         proprietario.apartamento,
                                                         proprietario.visitante
                                                     ))

    # Buscar todos veículos
    def buscar_todos_veiculos(self):
        veiculo = Veiculo.Veiculo()

        resposta = veiculo.buscarTodos()

        self.veiculosQuadroRegistros.delete(*self.veiculosQuadroRegistros.get_children())
        for veiculo in resposta:
            self.veiculosQuadroRegistros.insert('', END, text=str(veiculo.idveiculo),
                                                values=(
                                                    veiculo.tipo,
                                                    veiculo.marca,
                                                    veiculo.modelo,
                                                    veiculo.ano,
                                                    veiculo.cor,
                                                    veiculo.placa,
                                                    veiculo.cpf_proprietario,
                                                ))

    # Buscar todos proprietários
    def buscar_todas_entradas(self):
        entrada = Entrada.Entrada()

        resposta = entrada.buscarTodos()

        self.registrosQuadroRegistros.delete(*self.registrosQuadroRegistros.get_children())
        self.quadroRegistros.delete(*self.quadroRegistros.get_children())

        i = 0
        for entrada in resposta:
            self.registrosQuadroRegistros.insert('', END, text=entrada.idEntrada,
                                                 values=(
                                                     datetime.strftime(datetime.strptime(entrada.data_hora, "%Y-%m-%d "
                                                                                                            "%H:%M:%S.%f"),
                                                                       "%Y-%m-%d %H:%M:%S"),
                                                     entrada.proprietario,
                                                     entrada.veiculo,
                                                     entrada.visitante,
                                                     entrada.placa
                                                 ))
            if i < 5:
                self.quadroRegistros.insert('', END, text=datetime.strftime(datetime.strptime(entrada.data_hora,
                                                                                              "%Y-%m-%d %H:%M:%S.%f"),
                                                                            "%Y-%m-%d %H:%M:%S"),
                                            values=(
                                                entrada.proprietario,
                                                entrada.veiculo,
                                                entrada.visitante,
                                                entrada.placa
                                            ))
            i += 1

    # Inserir proprietário
    def cadastrar_proprietario(self):
        proprietario = Proprietario.Proprietario(
            0,
            str(self.cadastroProprietarioNome.get()),
            str(self.cadastroProprietarioCpf.get()),
            str(self.cadastroProprietarioTelefone.get()),
            str(self.cadastroProprietarioApartamento.get()),
            str(self.cadastroProprietarioVisitante.get())
        )

        resposta = proprietario.inserir()
        print(resposta)
        if "sucesso" in resposta:
            messagebox.showinfo("Sucesso", resposta)
            self.atualizar_cpfs()
            self.buscar_todos_proprietarios()
        else:
            messagebox.showerror("Erro", resposta)

        print(proprietario.descricao())

    # Inserir veículo
    def cadastrar_veiculo(self):
        if self.cpf_proprietario == "":
            messagebox.showwarning("Necessário vincular a um dono", "Campo de CPF do proprietário vazio. "
                                                                    "Impossível criar veículo sem um vinculo com "
                                                                    "um proprietário.")
            return
        veiculo = Veiculo.Veiculo(
            0,
            str(self.tipo_veiculo.get()),
            str(self.cadastroVeiculoCor.get()),
            str(self.cadastroVeiculoMarca.get()),
            str(self.cadastroVeiculoModelo.get()),
            str(self.cadastroVeiculoAno.get()),
            str(self.cadastroVeiculoPlaca.get()),
            str(self.cpf_proprietario.get())
        )

        resposta = veiculo.inserir()
        print(resposta)
        if "sucesso" in resposta:
            messagebox.showinfo("Sucesso", resposta)
            self.buscar_todos_veiculos()
        else:
            messagebox.showerror("Erro", resposta)

        print(veiculo.descricao())

    # Função atualizar CPFs disponíveis para a inserção de veículos
    def atualizar_cpfs(self):
        cpfs_proprietarios = Proprietario.Proprietario().buscarTodosCpfs()

        self.cadastroVeiculoCpfProprietario.pack_forget()
        if len(cpfs_proprietarios) > 0:
            self.cpf_proprietario.set(cpfs_proprietarios[0])

            self.cadastroVeiculoCpfProprietario = OptionMenu(self.frameRightTab2, self.cpf_proprietario,
                                                             *cpfs_proprietarios)
            self.cadastroVeiculoCpfProprietario["width"] = 25
            self.cadastroVeiculoCpfProprietario["font"] = self.fontePadrao
            self.cadastroVeiculoCpfProprietario["menu"].config(bg="white")
            self.cadastroVeiculoCpfProprietario.pack()

        else:
            self.cadastroVeiculoCpfProprietario = Label(self.frameRightTab2, text="Nenhum proprietário registrado...",
                                                        font=self.fontePadrao, padx=10, pady=10)
            self.cadastroVeiculoCpfProprietario.pack()

        self.cadastroVeiculoAtualizarCpfs.pack_forget()
        self.cadastroVeiculoAtualizarCpfs.pack(side=RIGHT)
        self.cadastroVeiculoConfirmar.pack_forget()
        self.cadastroVeiculoConfirmar.pack()

    # Pesquisar proprietario
    def pesquisar_proprietario(self):
        tipoPesquisa = self.pequisar_por_proprietario.get()
        valorPesquisa = self.alterarProprietarioPesquisar.get()

        proprietario = Proprietario.Proprietario().pesquisar(tipoPesquisa, valorPesquisa)

        if proprietario is not None:
            messagebox.showinfo("Sucesso", "Sucesso ao buscar proprietário!")
            self.proprietario_modificar = proprietario

            self.alterarProprietarioNome.delete(0, 'end')
            self.alterarProprietarioNome.insert(0, proprietario.nome)

            self.alterarProprietarioCpf.delete(0, 'end')
            self.alterarProprietarioCpf.insert(0, proprietario.cpf)

            self.alterarProprietarioTelefone.delete(0, 'end')
            self.alterarProprietarioTelefone.insert(0, proprietario.telefone)

            self.alterarProprietarioApartamento.delete(0, 'end')
            self.alterarProprietarioApartamento.insert(0, proprietario.apartamento)

            self.alterarProprietarioVisitante.delete(0, 'end')
            self.alterarProprietarioVisitante.insert(0, proprietario.visitante)

        else:
            messagebox.showerror("Falha", "Proprietário não encontrado! Verifique os campos de busca.")

    # Pesquisar veículo
    def pesquisar_veiculo(self):
        tipoPesquisa = self.pesquisar_por_veiculo.get()
        valorPesquisa = self.alterarVeiculoPesquisar.get()

        veiculo = Veiculo.Veiculo().pesquisar(tipoPesquisa, valorPesquisa)

        if veiculo is not None:
            messagebox.showinfo("Sucesso", "Sucesso ao buscar veículo!")
            self.veiculo_modificar = veiculo

            self.alterarVeiculoTipo.delete(0, 'end')
            self.alterarVeiculoTipo.insert(0, veiculo.tipo)

            self.alterarVeiculoCor.delete(0, 'end')
            self.alterarVeiculoCor.insert(0, veiculo.cor)

            self.alterarVeiculoMarca.delete(0, 'end')
            self.alterarVeiculoMarca.insert(0, veiculo.marca)

            self.alterarVeiculoModelo.delete(0, 'end')
            self.alterarVeiculoModelo.insert(0, veiculo.modelo)

            self.alterarVeiculoAno.delete(0, 'end')
            self.alterarVeiculoAno.insert(0, veiculo.ano)

            self.alterarVeiculoPlaca.delete(0, 'end')
            self.alterarVeiculoPlaca.insert(0, veiculo.placa)

            self.alterarVeiculoCpfProprietario.config(state=NORMAL)
            self.alterarVeiculoCpfProprietario.delete(0, 'end')
            self.alterarVeiculoCpfProprietario.insert(0, veiculo.cpf_proprietario)
            self.alterarVeiculoCpfProprietario.config(state=DISABLED)

        else:
            messagebox.showerror("Falha", "Veículo não encontrado! Verifique os campos de busca.")

    # Aterar proprietário
    def alterar_proprietario(self):
        if self.proprietario_modificar is not None:
            self.proprietario_modificar.nome = self.alterarProprietarioNome.get()
            self.proprietario_modificar.cpf = self.alterarProprietarioCpf.get()
            self.proprietario_modificar.telefone = self.alterarProprietarioTelefone.get()
            self.proprietario_modificar.apartamento = self.alterarProprietarioApartamento.get()
            self.proprietario_modificar.visitante = self.alterarProprietarioVisitante.get().upper()

            resposta = self.proprietario_modificar.atualizar()

            if "sucesso" in resposta:
                messagebox.showinfo("Sucesso", resposta)

                self.proprietario_modificar = None

                self.alterarProprietarioNome.delete(0, 'end')
                self.alterarProprietarioCpf.delete(0, 'end')
                self.alterarProprietarioTelefone.delete(0, 'end')
                self.alterarProprietarioApartamento.delete(0, 'end')
                self.alterarProprietarioVisitante.delete(0, 'end')

                self.atualizar_cpfs()
                self.buscar_todos_proprietarios()

            else:
                messagebox.showerror("Falha", resposta)
        else:
            messagebox.showwarning("Nenhum proprietário selecionado",
                                   "Pesquise um proprietário válido para ser alterado.")

    # Alterar  veículo
    def alterar_veiculo(self):
        if self.veiculo_modificar is not None:
            self.veiculo_modificar.tipo = self.alterarVeiculoTipo.get()
            self.veiculo_modificar.cor = self.alterarVeiculoCor.get()
            self.veiculo_modificar.marca = self.alterarVeiculoMarca.get()
            self.veiculo_modificar.modelo = self.alterarVeiculoModelo.get()
            self.veiculo_modificar.ano = self.alterarVeiculoAno.get()
            self.veiculo_modificar.placa = self.alterarVeiculoPlaca.get()

            resposta = self.veiculo_modificar.atualizar()

            if "sucesso" in resposta:
                messagebox.showinfo("Sucesso", resposta)

                self.veiculo_modificar = None

                self.alterarVeiculoTipo.delete(0, 'end')
                self.alterarVeiculoCor.delete(0, 'end')
                self.alterarVeiculoMarca.delete(0, 'end')
                self.alterarVeiculoModelo.delete(0, 'end')
                self.alterarVeiculoAno.delete(0, 'end')
                self.alterarVeiculoPlaca.delete(0, 'end')

                self.buscar_todos_veiculos()

            else:
                messagebox.showerror("Falha", resposta)
        else:
            messagebox.showwarning("Nenhum veículo selecionado",
                                   "Pesquise um veículo válido para ser alterado.")

    # Deletar proprietário
    def deletar_proprietario(self):
        if self.proprietario_modificar is not None:
            resposta = self.proprietario_modificar.deletar()

            if "sucesso" in resposta:
                messagebox.showinfo("Sucesso", resposta)

                self.proprietario_modificar = None

                self.alterarProprietarioNome.delete(0, 'end')
                self.alterarProprietarioCpf.delete(0, 'end')
                self.alterarProprietarioTelefone.delete(0, 'end')
                self.alterarProprietarioApartamento.delete(0, 'end')
                self.alterarProprietarioVisitante.delete(0, 'end')

                self.atualizar_cpfs()
                self.buscar_todos_proprietarios()

            else:
                messagebox.showerror("Falha", resposta)
        else:
            messagebox.showwarning("Nenhum proprietário selecionado",
                                   "Pesquise um proprietário válido para ser deletado.")

    # Deletar veículo
    def deletar_veiculo(self):
        if self.veiculo_modificar is not None:
            resposta = self.veiculo_modificar.deletar()

            if "sucesso" in resposta:
                messagebox.showinfo("Sucesso", resposta)

                self.veiculo_modificar = None

                self.alterarVeiculoTipo.delete(0, 'end')
                self.alterarVeiculoCor.delete(0, 'end')
                self.alterarVeiculoMarca.delete(0, 'end')
                self.alterarVeiculoModelo.delete(0, 'end')
                self.alterarVeiculoAno.delete(0, 'end')
                self.alterarVeiculoPlaca.delete(0, 'end')
                self.alterarVeiculoCpfProprietario.config(state=NORMAL)
                self.alterarVeiculoCpfProprietario.delete(0, 'end')
                self.alterarVeiculoCpfProprietario.config(state=DISABLED)

                self.buscar_todos_veiculos()

            else:
                messagebox.showerror("Falha", resposta)
        else:
            messagebox.showwarning("Nenhum veículo selecionado",
                                   "Pesquise um veículo válido para ser deletado.")

    # Função a ser criada, iniciada após o clique do botão 'Localizar'
    def localizar_placa(self):
        if DEBUG:
            caracteresPossivelPlaca = ""

            # Localizar AUTOMATICAMENTE placa através da imagem capturada
            if len(self.letras.get()) == 0 and len(self.numeros.get()) == 0:
                imgTeste = imread("capturasParaIdentificacao/teste2.jpg")
                possiveisPlacasIdentificadas = IdentificaPlaca.IdentificaPlaca(imgTeste,
                                                                               "teste",
                                                                               5000,
                                                                               100000).buscarPossiveisPlacas()

                print("Total Possíveis Placas Identificadas: " + str(len(possiveisPlacasIdentificadas)))

                for i, possivelPlaca in enumerate(possiveisPlacasIdentificadas):
                    identificacaoCorreta, caracteresPossivelPlaca = \
                        IdentificaCaracteres.IdentificaCaracteres(possivelPlaca).identificarCaracteres()

                    # Deletar todas as imagens de possíveis placas (limpar imagens desnecessarias)
                    files = glob.glob('possiveisPlacasIdentificadas/*')
                    for file in files:
                        os.remove(file)

                    if identificacaoCorreta:
                        messagebox.showinfo("Sucesso", "Caracteres identificados com sucesso! Placa: " +
                                            caracteresPossivelPlaca)
                        break

            # Localizar MANUALMENTE placa através da inserção do usuário
            elif len(self.letras.get()) != 3 and len(self.numeros.get()) != 4:
                messagebox.showwarning("Placa Inválida", "Informe um padrão de placa válido (e.x: XXX-0000).")
                return
            else:
                caracteresPossivelPlaca = self.letras.get() + "-" + self.numeros.get()

            veiculo = Veiculo.Veiculo().pesquisar("Placa", caracteresPossivelPlaca)

            if veiculo.idveiculo > 0:
                proprietario = Proprietario.Proprietario().pesquisar("CPF", veiculo.cpf_proprietario)

                # Preencher proprietário
                self.cpf.config(state=NORMAL)
                self.cpf.delete(0, END)
                self.cpf.insert(0, proprietario.cpf)
                self.cpf.config(state=DISABLED)

                self.nome.config(state=NORMAL)
                self.nome.delete(0, END)
                self.nome.insert(0, proprietario.nome)
                self.nome.config(state=DISABLED)

                self.telefone.config(state=NORMAL)
                self.telefone.delete(0, END)
                self.telefone.insert(0, proprietario.telefone)
                self.telefone.config(state=DISABLED)

                self.apartamento.config(state=NORMAL)
                self.apartamento.delete(0, END)
                self.apartamento.insert(0, proprietario.apartamento)
                self.apartamento.config(state=DISABLED)

                self.naoVisitante.config(state=NORMAL)
                self.simVisitante.config(state=NORMAL)
                if proprietario.visitante == "SIM":
                    self.visitante.set(1)
                elif proprietario.visitante == "NÃO":
                    self.visitante.set(0)
                self.naoVisitante.config(state=DISABLED)
                self.simVisitante.config(state=DISABLED)

                # Preencher proprietário
                self.cpf.config(state=NORMAL)
                self.cpf.delete(0, END)
                self.cpf.insert(0, proprietario.cpf)
                self.cpf.config(state=DISABLED)

                self.nome.config(state=NORMAL)
                self.nome.delete(0, END)
                self.nome.insert(0, proprietario.nome)
                self.nome.config(state=DISABLED)

                self.telefone.config(state=NORMAL)
                self.telefone.delete(0, END)
                self.telefone.insert(0, proprietario.telefone)
                self.telefone.config(state=DISABLED)

                self.apartamento.config(state=NORMAL)
                self.apartamento.delete(0, END)
                self.apartamento.insert(0, proprietario.apartamento)
                self.apartamento.config(state=DISABLED)

                if proprietario.visitante == "SIM":
                    self.visitante.set(1)
                elif proprietario.visitante == "NÃO":
                    self.visitante.set(0)

                # Preencher veículo
                self.tipo.config(state=NORMAL)
                self.tipo.delete(0, END)
                self.tipo.insert(0, veiculo.tipo)
                self.tipo.config(state=DISABLED)

                self.cor.config(state=NORMAL)
                self.cor.delete(0, END)
                self.cor.insert(0, veiculo.cor)
                self.cor.config(state=DISABLED)

                self.marca.config(state=NORMAL)
                self.marca.delete(0, END)
                self.marca.insert(0, veiculo.marca)
                self.marca.config(state=DISABLED)

                self.modelo.config(state=NORMAL)
                self.modelo.delete(0, END)
                self.modelo.insert(0, veiculo.modelo)
                self.modelo.config(state=DISABLED)

                self.ano.config(state=NORMAL)
                self.ano.delete(0, END)
                self.ano.insert(0, veiculo.ano)
                self.ano.config(state=DISABLED)

                self.placa.config(state=NORMAL)
                self.placa.delete(0, END)
                self.placa.insert(0, veiculo.placa)
                self.placa.config(state=DISABLED)

                cadastrar_entrada = messagebox.askyesno("Veículo Encontrado!", "Deseja inserir entrada?")
                if cadastrar_entrada:
                    entrada = Entrada.Entrada(
                        0,
                        str(datetime.now()),
                        proprietario.nome + ", " + proprietario.cpf,
                        veiculo.marca + " " + veiculo.modelo + ", " + veiculo.cor,
                        proprietario.visitante,
                        veiculo.placa
                    )
                    entrada.inserir()

                    self.buscar_todas_entradas()

                    messagebox.showinfo("Sucesso", "Entrada cadastrada.")
                else:
                    messagebox.showerror("Cancelado", "Entrada não cadastrada.")
            else:
                messagebox.showerror("Veículo não encontrado", "Placa '" + caracteresPossivelPlaca + "' não está vinculada a nenhum veículo.")

        # else:
            # cam = VideoCapture(0, CAP_DSHOW)  # 0 -> index of camera
            # s, img = cam.read()
            #
            # if s:  # frame captured without any errors
            #     # =========== Tirar foto com a câmera do NETEBOOK ou RASPBERRY =========
            #     # namedWindow("cam-test", WINDOW_AUTOSIZE)
            #     # imshow("cam-test", img)
            #     # waitKey(0)
            #     # destroyWindow("cam-test")
            #     # imwrite("placa.jpg", img)  # save image
            #
            #     # =========== Identificar Placa em Imagem ===========
            #     # original, preprocessada = PreProcessamentoPlacas.PreProcessamentoPlacas("identificarPlacas/105.jpg").preprocessar()
            #     # # imwrite("possiveisPlacasIdentificadas/placa_preprocesada.jpg", preprocessada)
            #     #
            #     # areaContornos = IdentificaPlaca.IdentificaPlaca(original, preprocessada, "identifica-placa", 40000,
            #     #                                                 9000000).desenharContornos()
            #
            #     (_, _, possiveisPlacasIdentificadas) = next(os.walk("possiveisPlacasIdentificadas"))
            #     for possivelPlaca in possiveisPlacasIdentificadas:
            #         # PreProcessamentoCaracteres.PreProcessamentoCaracteres("possiveisPlacasIdentificadas/" + possivelPlaca).preprocessar()
            #         possivelPlaca = imread("possiveisPlacasIdentificadas/" + possivelPlaca)
            #
            #         PreProcessamentoCaracteres.PreProcessamentoCaracteres(possivelPlaca).preprocessar()
            #         waitKey(0)
            #         destroyAllWindows()
            #
            #     # caracteres = pytess.image_to_string(preprocessada, lang='eng', config='--oem 3 --psm 5')
            #     #
            #     # # Printar no terminal o nome do arquivo juntamente aos caracteres reconhecidos (ex. '001.jpg: SIA-0231')
            #     # print(caracteres)
            #
            # placa = self.letras.get() + "-" + self.numeros.get()
            # veiculo = Veiculo.Veiculo().pesquisar("Placa", placa)
            #
            # if veiculo.idveiculo > 0:
            #     proprietario = Proprietario.Proprietario().pesquisar("CPF", veiculo.cpf_proprietario)
            #
            #     # Preencher proprietário
            #     self.cpf.config(state=NORMAL)
            #     self.cpf.delete(0, END)
            #     self.cpf.insert(0, proprietario.cpf)
            #     self.cpf.config(state=DISABLED)
            #
            #     self.nome.config(state=NORMAL)
            #     self.nome.delete(0, END)
            #     self.nome.insert(0, proprietario.nome)
            #     self.nome.config(state=DISABLED)
            #
            #     self.telefone.config(state=NORMAL)
            #     self.telefone.delete(0, END)
            #     self.telefone.insert(0, proprietario.telefone)
            #     self.telefone.config(state=DISABLED)
            #
            #     self.apartamento.config(state=NORMAL)
            #     self.apartamento.delete(0, END)
            #     self.apartamento.insert(0, proprietario.apartamento)
            #     self.apartamento.config(state=DISABLED)
            #
            #     self.naoVisitante.config(state=NORMAL)
            #     self.simVisitante.config(state=NORMAL)
            #     if proprietario.visitante == "SIM":
            #         self.visitante.set(1)
            #     elif proprietario.visitante == "NÃO":
            #         self.visitante.set(0)
            #     self.naoVisitante.config(state=DISABLED)
            #     self.simVisitante.config(state=DISABLED)
            #
            #     # Preencher proprietário
            #     self.cpf.config(state=NORMAL)
            #     self.cpf.delete(0, END)
            #     self.cpf.insert(0, proprietario.cpf)
            #     self.cpf.config(state=DISABLED)
            #
            #     self.nome.config(state=NORMAL)
            #     self.nome.delete(0, END)
            #     self.nome.insert(0, proprietario.nome)
            #     self.nome.config(state=DISABLED)
            #
            #     self.telefone.config(state=NORMAL)
            #     self.telefone.delete(0, END)
            #     self.telefone.insert(0, proprietario.telefone)
            #     self.telefone.config(state=DISABLED)
            #
            #     self.apartamento.config(state=NORMAL)
            #     self.apartamento.delete(0, END)
            #     self.apartamento.insert(0, proprietario.apartamento)
            #     self.apartamento.config(state=DISABLED)
            #
            #     if proprietario.visitante == "SIM":
            #         self.visitante.set(1)
            #     elif proprietario.visitante == "NÃO":
            #         self.visitante.set(0)
            #
            #     # Preencher veículo
            #     self.tipo.config(state=NORMAL)
            #     self.tipo.delete(0, END)
            #     self.tipo.insert(0, veiculo.tipo)
            #     self.tipo.config(state=DISABLED)
            #
            #     self.cor.config(state=NORMAL)
            #     self.cor.delete(0, END)
            #     self.cor.insert(0, veiculo.cor)
            #     self.cor.config(state=DISABLED)
            #
            #     self.marca.config(state=NORMAL)
            #     self.marca.delete(0, END)
            #     self.marca.insert(0, veiculo.marca)
            #     self.marca.config(state=DISABLED)
            #
            #     self.modelo.config(state=NORMAL)
            #     self.modelo.delete(0, END)
            #     self.modelo.insert(0, veiculo.modelo)
            #     self.modelo.config(state=DISABLED)
            #
            #     self.ano.config(state=NORMAL)
            #     self.ano.delete(0, END)
            #     self.ano.insert(0, veiculo.ano)
            #     self.ano.config(state=DISABLED)
            #
            #     self.placa.config(state=NORMAL)
            #     self.placa.delete(0, END)
            #     self.placa.insert(0, veiculo.placa)
            #     self.placa.config(state=DISABLED)
            #
            #     cadastrar_entrada = messagebox.askyesno("Veículo Encontrado!", "Deseja inserir entrada?")
            #     if cadastrar_entrada:
            #         entrada = Entrada.Entrada(
            #             0,
            #             str(datetime.now()),
            #             proprietario.nome + ", " + proprietario.cpf,
            #             veiculo.marca + " " + veiculo.modelo + ", " + veiculo.cor,
            #             proprietario.visitante,
            #             veiculo.placa
            #         )
            #         entrada.inserir()
            #
            #         self.buscar_todas_entradas()
            #
            #         messagebox.showinfo("Sucesso", "Entrada cadastrada.")
            #     else:
            #         messagebox.showerror("Cancelado", "Entrada não cadastrada.")
            # else:
            #     messagebox.showerror("Veículo não encontrado", "Placa '" + placa + "' não está vinculada a nenhum veículo.")


# Inicialização da interface gráfica principal da janela desenvolvida
# para o sistema
root = Tk()
root.title("Controle de Acesso Veicular Condominial")
imgicon = PhotoImage(file=os.path.join('icones/logo.png'))
root.tk.call('wm', 'iconphoto', root.w, imgicon)

# Full Screen
# - Windows
root.state('zoomed')
# - Linux
# root.attributes('-zoomed', True)

Interface(root)
root.mainloop()
