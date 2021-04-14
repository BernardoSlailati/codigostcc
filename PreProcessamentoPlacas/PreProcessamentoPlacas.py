# Autor: Bernardo Michel Slailati
# Arquivo: PreProcessamentoPlacas.py
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


# Classe PreProcessamentoPlacas
class PreProcessamento(object):
    # Construtor contendo como parâmetro o diretório da imagem a ser tratada
    def __init__(self, imagemOriginal=""):
        self.imagemOriginal = imagemOriginal

    # Ajuste de luminosidade na imagem
    @staticmethod
    def ajusteLuminosidade(imagem, gama=0.75):
        invGama = 1.0 / gama
        tabela = np.array([((i / 255.0) ** invGama) * 255
                           for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(imagem, tabela)

    # Método que aplica o pré-processamento adequado a imagem
    def preprocessar(self):
        try:
            imshow("IDENTIFICA PLACA - original", self.imagemOriginal[::3, ::3])
            waitKey(0)

            # Ajuste de luminosidade
            ajusteLuminosidade = self.ajusteLuminosidade(self.imagemOriginal)
            imshow("IDENTIFICA PLACA - ajuste luminosidade", ajusteLuminosidade[::3, ::3])
            waitKey(0)

            # Transformação da imagem para escala cinza
            cinza = cvtColor(ajusteLuminosidade, COLOR_BGR2GRAY)
            imshow("IDENTIFICA PLACA - cinza", cinza[::3, ::3])
            waitKey(0)

            # Aplicação do método de erosão na imagem em escala cinza
            kernelErosao = np.ones((5, 5), np.uint8)
            erosao = erode(cinza, kernelErosao)
            imshow("IDENTIFICA PLACA - erosao", erosao[::3, ::3])
            waitKey(0)

            # Aplicação do método de dilatação na imagem erodizada
            kernelDilatacao = np.ones((3, 3), np.uint8)
            dilatacao = dilate(erosao, kernelDilatacao, iterations=3)
            imshow("IDENTIFICA PLACA - dilatacao", dilatacao[::3, ::3])
            waitKey(0)

            # Aplicação do método de limiarização adaptativa na imagem
            # dilatada
            limiarizacao = adaptiveThreshold(dilatacao, 255,
                                             ADAPTIVE_THRESH_MEAN_C,
                                             THRESH_BINARY, 45, 7)

            # Variável contendo a imagem pré-processada
            preprocessada = limiarizacao[::3, ::3]

            imshow("IDENTIFICA PLACA - limiarizacao", preprocessada)
            waitKey(0)
            destroyAllWindows()

            # Retorno da imagem original e pré-processada
            return preprocessada

        # Em caso de falha na utilização da função, mostra-se no
        # terminal uma mensagem de erro
        except:
            print("Erro ao carregar imagem...")