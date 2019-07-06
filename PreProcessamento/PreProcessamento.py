# Autor: Bernardo Michel Slailati
# Arquivo: PreProcessamento.py
# Função: Realizar o pré-processamento adequado as imagensTeste de veículos
# contendo placas veiculares a serem posteriormente identificadas.

# Importação das bibliotecas necessárias
from cv2 import *
import numpy as np

# Diretórios 'imagensTeste' e 'resultadosPreprocessamento', referentes as
# pastas contendo as imagens utilizadas nos testes e resultados do
# pré-processamento, respectivamente
IMAGENS_DIR = "imagensTeste/"
RESULTADOS_DIR = "resultadosPreprocessamento/"

# Classe PreProcessamento
class PreProcessamento(object):
    # Construtor contendo como parâmetro o diretório da imagem a ser tratada
    def __init__(self, imageDir=""):
        self.imageDir = imageDir

    # Ajuste de luminosidade na imagem
    def ajusteLuminosidade(self, imagem, gama=0.75):
        invGama = 1.0 / gama
        tabela = np.array([((i / 255.0) ** invGama) * 255
                           for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(imagem, tabela)

    # Método que aplica o pré-processamento adequado a imagem
    def preprocessar(self):
        try:
            # Carrega imagem original a partir do diretório passado como
            # parâmetro para a clase 'PreProcessamento'
            original = imread(self.imageDir)
            original = self.ajusteLuminosidade(original)

            # Transformação da imagem para escala cinza
            cinza = cvtColor(original, COLOR_BGR2GRAY)

            # Aplicação do método de erosão na imagem em escala cinza
            kernelErosao = np.ones((7, 7), np.uint8)
            erosao = erode(cinza, kernelErosao)

            # Aplicação do método de dilatação na imagem erodizada
            kernelDilatacao = np.ones((3, 3), np.uint8)
            dilatacao = dilate(erosao, kernelDilatacao, iterations=5)

            # Aplicação do método de limiarização adaptativa na imagem
            # dilatada
            limiarizacao = adaptiveThreshold(dilatacao, 255,
                                             ADAPTIVE_THRESH_MEAN_C,
                                             THRESH_BINARY, 41, 5)

            # Variável contendo a imagem pré-processada
            preprocessada = limiarizacao

            # Retorno da imagem original e pré-processada
            return original, preprocessada

        # Em caso de falha na utilização da função, mostra-se no
        # terminal uma mensagem de erro
        except:
            print("Erro ao carregar imagem...")

        # Aplicação do pré-processamento em todas as imagens
        # contidas na pasta 'imagensTeste', sendo salvas as
        # imagens resultantes na pasta
        # 'resultadosIdentificacaoPlacas'
        def preprocessarImagensTeste(diretorioImagensTeste):
            # Lista 'filenames' contendo os nomes de todos
            # os arquivos contidos na pasta 'imagensTeste'
            (_, _, filenames) = next(os.walk
                                     (diretorioImagensTeste))

            for filename in filenames:
                print(filename)
                original, preprocessada = \
                    PreProcessamento(diretorioImagensTeste
                                     + filename).preprocessar()
                imwrite(RESULTADOS_DIR + filename, preprocessada)


pp = PreProcessamento(IMAGENS_DIR + "026.jpg")
_, preprocessada = pp.preprocessar()
imwrite(RESULTADOS_DIR + "026.jpg", preprocessada)