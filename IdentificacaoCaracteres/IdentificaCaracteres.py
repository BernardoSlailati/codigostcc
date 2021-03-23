# Autor: Bernardo Michel Slailati
# Arquivo: IdentificaCaracteres.py
# Função: Realizar a identificação dos caracteres do conjunto de imagens
# específico para testes (imagens previamente recortadas, contendo apenas
# as regiões das placas, já em formato binarizado).

# Importação das bibliotecas necessárias
import pytesseract as pytess
from cv2 import *
import os

try:
    from PIL import Image
except ImportError:
    import Image

# Diretórios 'imagensPlacasTeste' e 'resultadosPreprocessamento', referentes
# as pastas contendo as imagens utilizadas nos testes e resultados da
# identificação das placas, respectivamente
IMAGENS_DIR = "imagensPlacasTeste/"
RESULTADOS_DIR = "resultadosIdentificacaoPlacas/"

# Lista 'filenames' contendo os nomes de todos
# os arquivos contidos na pasta 'imagensPlacasTeste'
(_, _, filenames) = next(os.walk(IMAGENS_DIR))
pytess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Identifica os caracteres de todas as imagens contidas no diretório 'imagensPlacasTeste'
for filename in sorted(filenames):
    # Comando para identificar os caracteres em imagens, gerando como resposta
    # um váriavel de texto contendo os caracteres concatenados
    placa = imread(IMAGENS_DIR + filename, CV_8UC1)

    # placaProcessada = blur(placa, (9, 9), 3)
    # placaProcessada = adaptiveThreshold(placaProcessada, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 75, 10)
    #
    # imshow("placaProcessada", placaProcessada)
    # waitKey(0)

    caracteres = pytess.image_to_string(placa, lang='man')

    # Printar no terminal o nome do arquivo juntamente aos caracteres reconhecidos (ex. '001.jpg: SIA-0231')
    print(filename + ": " + caracteres)