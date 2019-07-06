# Autor: Bernardo Michel Slailati
# Arquivo: Interface.py
# Função: Criar interface gráfica referente a janela
# principal do software a ser desenvolvido.

# Importação das bibliotecas necessárias
from tkinter import *
from tkinter import ttk
import pytesseract
from PIL import Image, ImageTk
from cv2 import *
import numpy as np
import re
from datetime import datetime

# Classe Interface
class Interface:
    # Construtor contendo como parâmetro o objeto de interface
    # disponibilidado pela biblioteca Tkinter
    def __init__(self, master=None):

        # Determinar fonte padrão a ser utilizada nos textos
        self.fontePadrao = ("Comic Sans MS", "12")

        # Fragmento lateral esquerdo da janela
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 50
        self.primeiroContainer.pack(side=LEFT)

        # Fragmento lateral direito da janela
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 50
        self.segundoContainer.pack(side=RIGHT)

        # Fragmento superior da janela
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 50
        self.terceiroContainer.pack(side=TOP)

        # Fragmento inferior da janela
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 50
        self.quartoContainer.pack(fill=BOTH, side=BOTTOM)


        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL ESQUERDO
        # ---------------------------------------------------------------
        image = Image.open("icones/placa.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 4),
                                                 int(height / 4)),
                                                Image.ANTIALIAS))

        self.titulo = Label(self.primeiroContainer, text="Placa Identificada")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.imagemPlaca = Label(self.primeiroContainer, image=photo)
        self.imagemPlaca.image = photo
        self.imagemPlaca.pack(side=LEFT)

        self.letrasLabel = Label(self.primeiroContainer, text="Letras:",
                                 font=self.fontePadrao)
        self.letrasLabel.pack()

        self.letras = Entry(self.primeiroContainer)
        self.letras["width"] = 25
        self.letras["font"] = self.fontePadrao
        self.letras.pack()

        self.numerosLabel = Label(self.primeiroContainer, text="Números:",
                                  font=self.fontePadrao)
        self.numerosLabel.pack()

        self.numeros = Entry(self.primeiroContainer)
        self.numeros["width"] = 25
        self.numeros["font"] = self.fontePadrao
        self.numeros.pack()

        self.confirmar = Button(self.primeiroContainer, padx=10, pady=10)
        self.confirmar["text"] = "LOCALIZAR"
        self.confirmar["font"] = ("Comics Sans MS", "8", "bold")
        self.confirmar["width"] = 12
        self.confirmar["command"] = self.localizarPlaca
        self.confirmar.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento LATERAL DIREITO
        # ---------------------------------------------------------------
        self.titulo = Label(self.segundoContainer, text="Veículo")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        image = Image.open("icones/veiculo.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 4),
                                                 int(height / 4)),
                                                Image.ANTIALIAS))

        self.imagemVeiculo = Label(self.segundoContainer, image=photo)
        self.imagemVeiculo.image = photo
        self.imagemVeiculo.pack(side=LEFT)

        self.tipoLabel = Label(self.segundoContainer, text="Tipo:",
                               font=self.fontePadrao)
        self.tipoLabel.pack()

        self.tipo = Entry(self.segundoContainer)
        self.tipo["width"] = 25
        self.tipo["font"] = self.fontePadrao
        self.tipo.pack()

        self.corLabel = Label(self.segundoContainer, text="Cor:",
                              font=self.fontePadrao)
        self.corLabel.pack()

        self.cor = Entry(self.segundoContainer)
        self.cor["width"] = 25
        self.cor["font"] = self.fontePadrao
        self.cor.pack()

        self.marcaLabel = Label(self.segundoContainer, text="Marca:",
                                font=self.fontePadrao)
        self.marcaLabel.pack()

        self.marca = Entry(self.segundoContainer)
        self.marca["width"] = 25
        self.marca["font"] = self.fontePadrao
        self.marca.pack()

        self.modeloLabel = Label(self.segundoContainer, text="Modelo:",
                                 font=self.fontePadrao)
        self.modeloLabel.pack()

        self.modelo= Entry(self.segundoContainer)
        self.modelo["width"] = 25
        self.modelo["font"] = self.fontePadrao
        self.modelo.pack()

        self.anoLabel = Label(self.segundoContainer, text="Ano:",
                              font=self.fontePadrao)
        self.anoLabel.pack()

        self.ano = Entry(self.segundoContainer)
        self.ano["width"] = 25
        self.ano["font"] = self.fontePadrao
        self.ano.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento SUPERIOR
        # ---------------------------------------------------------------
        self.datahora = Label(self.terceiroContainer)
        self.datahora["font"] = ("Comic Sans MS", "10", "bold")
        self.datahora.pack(side=TOP)

        image = Image.open("icones/relogio.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 4),
                                                 int(height / 4)),
                                                Image.ANTIALIAS))

        self.relogio = Label(self.terceiroContainer, image=photo)
        self.relogio.image = photo
        self.relogio.pack()

        image = Image.open("icones/proprietario.png")
        [width, height] = image.size
        photo = ImageTk.PhotoImage(image.resize((int(width / 6),
                                                 int(height / 6)),
                                                Image.ANTIALIAS))

        self.titulo = Label(self.terceiroContainer, text="Proprietário/Visitante")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.imagemPessoa = Label(self.terceiroContainer, image=photo)
        self.imagemPessoa.image = photo
        self.imagemPessoa.pack(side=LEFT)

        self.nomeLabel = Label(self.terceiroContainer, text="Tipo:",
                               font=self.fontePadrao)
        self.nomeLabel.pack()

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 25
        self.nome["font"] = self.fontePadrao
        self.nome.pack()

        self.cpfLabel = Label(self.terceiroContainer, text="CPF:",
                              font=self.fontePadrao)
        self.cpfLabel.pack()

        self.cpf = Entry(self.terceiroContainer)
        self.cpf["width"] = 25
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack()

        self.telefoneLabel = Label(self.terceiroContainer, text="Telefone:",
                                   font=self.fontePadrao)
        self.telefoneLabel.pack()

        self.telefone = Entry(self.terceiroContainer)
        self.telefone["width"] = 25
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack()

        self.apartamentoLabel = Label(self.terceiroContainer,
                                      text="Modelo:", font=self.fontePadrao)
        self.apartamentoLabel.pack()

        self.apartamento = Entry(self.terceiroContainer)
        self.apartamento["width"] = 25
        self.apartamento["font"] = self.fontePadrao
        self.apartamento.pack()

        self.visitanteLabel = Label(self.terceiroContainer, text="Visitante:",
                                    font=self.fontePadrao)
        self.visitanteLabel.pack()

        self.visitante = IntVar()

        self.simVisitante = Radiobutton(self.terceiroContainer, text="NÃO",
                                        variable=self.visitante, value=0)
        self.simVisitante["width"] = 25
        self.simVisitante["font"] = self.fontePadrao
        self.simVisitante.pack()

        self.naoVisitante = Radiobutton(self.terceiroContainer, text="SIM",
                                        variable=self.visitante, value=1)
        self.naoVisitante["width"] = 25
        self.naoVisitante["font"] = self.fontePadrao
        self.naoVisitante.pack()

        # ---------------------------------------------------------------
        # Criação dos elementos visuais do fragmento INFERIOR
        # ---------------------------------------------------------------
        self.titulo = Label(self.quartoContainer, text="Últimos registros:")
        self.titulo["font"] = ("Comic Sans MS", "14", "bold")
        self.titulo.pack()

        self.quadroRegistros = ttk.Treeview(self.quartoContainer,
                                            columns=("Data e Hora",
                                                     "Proprietário",
                                                     "Veículo", "Visitante",
                                                     "Placa"))
        self.quadroRegistros.heading('#0', text='Data e Hora', anchor=CENTER)
        self.quadroRegistros.heading('#1', text='Proprietário', anchor=CENTER)
        self.quadroRegistros.heading('#2', text='Veículo', anchor=CENTER)
        self.quadroRegistros.heading('#3', text='Visitante', anchor=CENTER)
        self.quadroRegistros.heading('#4', text='Placa', anchor=CENTER)

        self.quadroRegistros.column('#0', stretch=YES, anchor=CENTER)
        self.quadroRegistros.column('#1', stretch=YES, anchor=CENTER)
        self.quadroRegistros.column('#2', stretch=YES, anchor=CENTER)
        self.quadroRegistros.column('#3', stretch=YES, anchor=CENTER)
        self.quadroRegistros.column('#4', stretch=YES, anchor=CENTER)

        self.i = 0
        self.quadroRegistros.pack()

        self.definirDataHora()

    # Função a ser criada, iniciada após o clique do botão 'Localizar'
    def localizarPlaca(self):
        pass

    # Função que fornece a data e hora atual a caixa de texto específica
    def definirDataHora(self):
        datetimenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datahora.config(text=datetimenow)

# Inicialização da interface gráfica principal da janela desenvolvida
# para o sistema
root = Tk()
root.title("Controle de Acesso Veicular Condominial")
imgicon = PhotoImage(file=os.path.join('icones/logo.png'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)
Interface(root)
root.mainloop()
