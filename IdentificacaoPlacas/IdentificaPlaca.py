# Autor: Bernardo Michel Slailati
# Arquivo: IdentificaPlaca.py
# Função: Realizar a identificação das placas do conjunto de imagens
# para testes.

# Importação das bibliotecas necessárias
from tkinter import *
from cv2 import *
from PreProcessamento import PreProcessamento as PP

# Diretórios 'imagensTeste' e 'resultadosPreprocessamento', referentes
# as pastas contendo as imagens utilizadas nos testes e resultados do
# pré-processamento, respectivamente
IMAGENS_DIR = "imagensTeste/"
RESULTADOS_DIR = "resultadosIdentificacaoPlacas/"

# Lista 'filenames' contendo os nomes de todos
# os arquivos contidos na pasta 'imagensTeste'
(_, _, filenames) = next(os.walk(IMAGENS_DIR))

# Classe IdentificaPlaca
class IdentificaPlaca(object):
    # Construtor contendo como parâmetros a imagem original, imagem
    # pré-processada, nome do arquivo a ser salvo, valores mínimo e
    # máximo de área para filtrar os contornos encontrados e margem
    # de erro aplicado a esses limites
    def __init__(self, imagemOriginal, imagemPreProcessada, nomeArquivo="",
                 areaMin=0, areaMax=0, margemErro=0):
        self.imagemOriginal = imagemOriginal
        self.imagemPreProcessada = imagemPreProcessada
        self.nomeArquivo = nomeArquivo
        self.areaMin = areaMin
        self.areaMax = areaMax
        self.margemErro = margemErro

    # Função que desenha os contornos encontrados, após o processo de
    # filtragem, na imagem original passada como parâmetro
    def desenharContornos(self):
        # Encontra todos os contornos na imagem
        contornos, _ = findContours(self.imagemPreProcessada, RETR_TREE,
                                    CHAIN_APPROX_SIMPLE)
        areasContornos = []

        num_cont = 1
        for i, contorno in enumerate(contornos):
            # Obteção do valor de área de cada contorno
            area = contourArea(contorno)
            # Filtro para escolha dos contornos adequados
            if self.areaMin - self.margemErro < area < self.areaMax +\
                    self.margemErro:
                num_cont += 1
                areasContornos.append(area)

                # Recorta o contorno da imagem original
                x, y, w, h = boundingRect(contorno)
                cortada = self.imagemOriginal[y:h + y, x:w + x]

                # Salva imagem recortada na pasta 'possiveisPlacas'
                imwrite("possiveisPlacas/" + self.nomeArquivo.replace(".jpg",
                                                                      "")
                        + "_" + str(area).replace(".", "-") + ".jpg", cortada)


                # Desenha o contorno na imagem original na cor amarelo
                drawContours(self.imagemOriginal, contorno, -1, (0, 255, 255),
                             10)

        # Salva imagem original com o desenho dos contornos na pasta
        # 'resultadosIdentificacaoPlacas'
        imwrite(RESULTADOS_DIR + self.nomeArquivo, self.imagemOriginal)
        # Mostra a imagem original com os contornos na tela
        imshow("Contornos", self.imagemOriginal[::3, ::3])
        waitKey(0)

        return areasContornos

# Classe que cria os elementos de interface a serem mostrados
class Application(Frame):
    # Construtor contendo os elementos: botão, caixa de opções e caixa
    # de texto
    def __init__(self, master):
        super(Application, self).__init__(master)

        self.button = Button(self, text='Localizar', command=self.localizar)
        self.spinbox = Spinbox(self, values=sorted(filenames))
        self.label1 = Label(self, text='Imagens:')

        self.grid()
        self.create_widgets()
    # Função que define a posição dos elementos visuais na tela
    def create_widgets(self):
        self.label1.grid(row=0, column=0, sticky=W)

        self.spinbox.grid(row=0, column=1, sticky=W)

        self.button.grid(row=1, column=1, sticky=W)
    # Função de clique do botão, para realizar o processo de identificação
    # das placas na imagem selecionada
    def localizar(self):
        # Diretório contendo a imagem selecionada pelo usuário
        imagedir = IMAGENS_DIR + self.spinbox.get()

        # Objeto que realiza a aplicação do algoritmo de pré-processamento
        # nas imagens
        preProcessamento = PP.PreProcessamento(imagedir)
        original, preprocessada = preProcessamento.preprocessar()

        # Processo de identificação das placas, retorna os valores de
        # áreas dos contornos encontrados
        areasContornos = IdentificaPlaca(original, preprocessada,
                                         self.spinbox.get(), 25000,
                                         900000, 0).desenharContornos()
        # Printa no terminal esses valores
        print('Areas contornadas: ', areasContornos)


# Interface gráfica simples que fornece ao usuário a opção de escolher
# de qual arquivo da pasta 'imagensTeste' deseja identificar a placa
root = Tk()
root.title('Teste Identificar Placas')
root.geometry('300x80')
app = Application(root)
app.mainloop()
