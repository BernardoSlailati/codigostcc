# Autor: Bernardo Michel Slailati
# Arquivo: PreProcessamentoPlacas.py
# Função: Realizar o pré-processamento adequado as imagens de placas
# veiculares brasileiras a serem posteriormente identificados seus
# caracteres.

# Importação das bibliotecas necessárias
from cv2 import *
import numpy as np


# Classe PreProcessamentoPlacas
class PreProcessamentoCaracteres(object):
    # Construtor contendo como parâmetro o diretório da imagem a ser tratada
    def __init__(self, imagemPossivelPlaca="", gama=0.75, threshold=127):
        self.imagemPossivelPlaca = imagemPossivelPlaca
        self.gama = gama
        self.threshold = threshold

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
            # Carrega imagem original a partir do diretório passado como
            # parâmetro para a clase 'PreProcessamentoPlacas'
            original = self.imagemPossivelPlaca
            imshow("IDENTIFICA CARACTERES - original", original)
            waitKey(0)

            # Cortar a imagem da placa original para capturar apenas os caracteres alvos de serem identificados
            # baseado nas proporções padrão de placas
            height, width, _ = original.shape
            original = original[int(0.33 * height): int(height * 0.9), int(0.05 * width): int(0.95 * width)]
            imshow("IDENTIFICA CARACTERES - original otimizada", original)
            waitKey(0)

            original = self.ajusteLuminosidade(original, self.gama)
            imshow("IDENTIFICA CARACTERES - ajusteLuminosidade", original)
            waitKey(0)
            # imwrite("original_iluminada.png", original)

            # Transformação da imagem para escala cinza
            cinza = cvtColor(original, COLOR_BGR2GRAY)
            imshow("IDENTIFICA CARACTERES - cinza", cinza)
            waitKey(0)
            # imwrite("cinza.png", cinza)

            bilateralFiltered = bilateralFilter(cinza, 11, 25, 25)
            imshow("IDENTIFICA CARACTERES - filtro bilateral", bilateralFiltered)
            waitKey(0)
            # imshow("bilateralFiltered", bilateralFiltered)
            # imwrite("bilateralFiltered.png", bilateralFiltered)

            _, limiarizacao = threshold(bilateralFiltered, self.threshold, 255, THRESH_OTSU)
            imshow("IDENTIFICA CARACTERES - limiarizacao", limiarizacao)
            waitKey(0)
            # imwrite("limiarizacao.png", limiarizacao)
            destroyAllWindows()

            return limiarizacao

        # Em caso de falha na utilização da função, mostra-se no
        # terminal uma mensagem de erro
        except:
            print("Erro ao carregar imagem...")
