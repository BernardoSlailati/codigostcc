# Autor: Bernardo Michel Slailati
# Arquivo: PreProcessamento.py
# Função: Realizar o pré-processamento adequado as imagensTeste de veículos
# contendo placas veiculares a serem posteriormente identificadas.

# Importação das bibliotecas necessárias
from cv2 import *
import numpy as np
import pytesseract as pytess

# Diretórios 'imagensTeste' e 'resultadosPreprocessamento', referentes as
# pastas contendo as imagens utilizadas nos testes e resultados do
# pré-processamento, respectivamente
# IMAGENS_DIR = "testeEntr/"
# RESULTADOS_DIR = "testRes/"

pytess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


# Classe PreProcessamento
class PreProcessamentoCaracteres(object):
    # Construtor contendo como parâmetro o diretório da imagem a ser tratada
    def __init__(self, image=""):
        self.image = image

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
            original = self.image

            height, width, _ = original.shape
            original = original[int(0.33 * height): int(height * 0.9), int(0.05 * width): int(0.95 * width)]


            caracteres = ""
            i = 1
            while len(caracteres) < 7 and i <= 40:
                original = self.ajusteLuminosidade(original, 1.05 ** i * 0.75)
                i += 1
                # imshow("original", original)
                imwrite("original_iluminada.png", original)

                # Transformação da imagem para escala cinza
                cinza = cvtColor(original, COLOR_BGR2GRAY)
                imwrite("cinza.png", cinza)

                # blured = bilateralFilter(cinza, 7, 35, 35)
                bilateralFiltered = bilateralFilter(cinza, 31, 75, 75)
                imshow("bilateralFiltered", bilateralFiltered)
                imwrite("bilateralFiltered.png", bilateralFiltered)

                # # Aplicação do método de erosão na imagem em escala cinza
                # kernelErosao = np.ones((7, 7), np.uint8)
                # erosao = erode(blured, kernelErosao)
                # imshow("erosao", erosao)
                #
                # # Aplicação do método de dilatação na imagem erodizada
                # kernelDilatacao = np.ones((5, 5), np.uint8)
                # dilatacao = dilate(erosao, kernelDilatacao)
                # imshow("dilatacao", dilatacao)

                # limiarizacao = adaptiveThreshold(blured, 255, ADAPTIVE_THRESH_GAUSSIAN_C,
                #                                  THRESH_BINARY, 31, 7)

                _, limiarizacao = threshold(bilateralFiltered, 127, 255, THRESH_OTSU)
                imshow("limiarizacao", limiarizacao)
                imwrite("limiarizacao.png", limiarizacao)

                caracteres = pytess.image_to_string(limiarizacao, lang='eng', config='--oem 3 --psm 13')\
                    .upper().replace("\n", "").replace("\f", "").replace("|", "1").replace(" ", "").replace("_", "").replace("]", "1")\
                    .replace(")", "1").replace(":", "-").replace("=", "")

                if caracteres.find("-") > -1:
                    placa = caracteres.split("-")

                    letras = placa[0].replace("0", "O").replace("1", "L")
                    numeros = placa[1]

                    print("---Placa Identificada---")
                    print(caracteres)
                    print("Letras: ")
                    print(letras)
                    print("Números: ")
                    print(numeros)
                    print("------------------------")


            # return original, original
            return original, limiarizacao

        # Em caso de falha na utilização da função, mostra-se no
        # terminal uma mensagem de erro
        except:
            print("Erro ao carregar imagem...")

#
# (_, _, filenames) = next(os.walk(IMAGENS_DIR))
#
# for filename in filenames:
#     pp = PreProcessamentoCaracteres(IMAGENS_DIR + filename)
#     _, preprocessada = pp.preprocessar()
#     imwrite(RESULTADOS_DIR + filename, preprocessada)
