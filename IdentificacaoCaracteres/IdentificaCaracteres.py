# Autor: Bernardo Michel Slailati
# Arquivo: IdentificaCaracteres.py
# Função: Realizar a identificação dos caracteres de imagens de
# placas veiculares brasileiras

# Importação das bibliotecas necessárias
import pytesseract as pytess
from cv2 import *
import os
from PreProcessamentoCaracteres import PreProcessamentoCaracteres

pytess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


# Classe IdentificaCaracteres
class IdentificaCaracteres(object):
    # Construtor contendo como parâmetros a imagem original, imagem
    # pré-processada, nome do arquivo a ser salvo, valores mínimo e
    # de erro aplicado a esses limites
    def __init__(self, imagemPossivelPlacaRecortada):
        self.imagemPossivelPlacaRecortada = imagemPossivelPlacaRecortada

    # Função que busca possíveis placas na imagem. desenha os contornos encontrados,
    # após o processo de pré-processamento na imagem original passada como parâmetro
    def identificarCaracteres(self):
        caracteres = ""
        i = 1
        while len(caracteres) < 7 and i <= 40:
            placaPreprocessadaCaracteres = \
                PreProcessamentoCaracteres.PreProcessamentoCaracteres(
                    self.imagemPossivelPlacaRecortada,
                    1.05 * i * 0.75
                ).preprocessar()

            caracteres = pytess.image_to_string(placaPreprocessadaCaracteres, lang='eng',
                                                config='--oem 3 --psm 13 -c tessedit_char_whitelist=0123456789'
                                                       '-ABCDEFGHIJKLMNOPQRSTUVXWYZ') \
                .upper().replace("\n", "").replace("\f", "").replace("|", "1").replace(" ", "").replace("_", "") \
                .replace("]", "1").replace(")", "1").replace(":", "-").replace("=", "")

            print(caracteres)

            if caracteres.find("-") > -1:
                placa = caracteres.split("-")

                letras = placa[0].replace("0", "O").replace("1", "L")
                numeros = placa[1].replace("O", "0").replace("L", "1").replace("I", "1")

                if len(letras) == 3 and len(numeros) == 4:
                    return True, letras + "-" + numeros
                else:
                    return False, letras + "-" + numeros

            else:
                return False, caracteres
