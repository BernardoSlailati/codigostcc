# Autor: Bernardo Michel Slailati
# Arquivo: IdentificaPlaca.py
# Função: Realizar a identificação das placas do conjunto de imagens
# para testes.

# Importação das bibliotecas necessárias
from tkinter import *
from cv2 import *
from PreProcessamentoPlacas import PreProcessamentoPlacas
import numpy as np

# Diretórios 'imagensTeste' e 'resultadosPreprocessamento', referentes
# as pastas contendo as imagens utilizadas nos testes e resultados de possíveis
# placas encontradas, respectivamente
IMAGENS_TESTE_DIR = "imagensTeste/"
POSSIVEIS_PLACAS_DIR = "possiveisPlacasIdentificadas/"


# Classe IdentificaPlaca
class IdentificaPlaca(object):
    # Construtor contendo como parâmetros a imagem original, imagem
    # pré-processada, nome do arquivo a ser salvo, valores mínimo e
    # de erro aplicado a esses limites
    def __init__(self, imagemOriginal, nomeArquivo="teste", areaMin=0, areaMax=0, margemErro=0):
        self.imagemOriginal = imagemOriginal
        self.imagemPreProcessada = PreProcessamentoPlacas.PreProcessamento(imagemOriginal).preprocessar()
        self.nomeArquivo = nomeArquivo
        self.areaMin = areaMin
        self.areaMax = areaMax
        self.margemErro = margemErro

    # Função que busca possíveis placas na imagem. desenha os contornos encontrados,
    # após o processo de pré-processamento na imagem original passada como parâmetro
    def buscarPossiveisPlacas(self):
        # Encontra todos os contornos na imagem
        contornos, _ = findContours(self.imagemPreProcessada, RETR_TREE, CHAIN_APPROX_SIMPLE)

        possiveisPlacasIdentificadas = []
        num_cont = 1

        originalASerCortada = self.imagemOriginal.copy()[::3, ::3]
        originalASerContornada = self.imagemOriginal.copy()[::3, ::3].astype(np.uint8)

        for i, contorno in enumerate(contornos):
            # Obteção do valor de área de cada contorno
            area = contourArea(contorno)

            # Filtro para escolha dos contornos adequados
            if self.areaMin - self.margemErro < area < self.areaMax + self.margemErro:

                # Recorta o contorno da imagem original
                x, y, w, h = boundingRect(contorno)
                cortada = originalASerCortada[y:h + y, x:w + x].copy()

                imshow("CONTORNOS - possivel placa cortada (" + str(num_cont) + ")", cortada)
                waitKey(0)

                possiveisPlacasIdentificadas.append(cortada)

                # Salva imagem recortada na pasta 'possiveisPlacasIdentificadas'
                imwrite("possiveisPlacasIdentificadas/" + self.nomeArquivo + str(num_cont)
                        + "_" + str(area).replace(".", "-") + ".jpg", cortada)

                # Desenha o contorno na imagem original na cor amarelo
                drawContours(originalASerContornada, contorno, -1, (0, 255, 255), 10)

                num_cont += 1

        # Mostrar contornos encontrados na placa original
        imshow("CONTORNOS - placa original", originalASerContornada)
        waitKey(0)
        destroyAllWindows()

        return possiveisPlacasIdentificadas