from cv2 import *
from pytesseract import *
import numpy as np

img = imread("Imagens/G.jpg", 0)
print(np.median(img))

invGama = 1.0 / 0.5
tabela = np.array([((i / 255.0) ** invGama) * 255
                   for i in np.arange(0, 256)]).astype("uint8")

img = LUT(img, tabela)

kernel = np.ones((7, 7), np.uint8)
morph = morphologyEx(img, MORPH_OPEN, kernel, iterations=3)

_, bin = threshold(morph, 80, 255, THRESH_BINARY)
#bin = adaptiveThreshold(img, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 7, 3)

# contours, _ = findContours(bin, RETR_TREE, CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     drawContours(img, contour, 0, (255, 255, 0))


# -psm N
# Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for N are:
# 10 = Treat the image as a single character.

print("amh: " + image_to_string(img, 'amh', config='-psm 10'))
print("eng: " + image_to_string(img, 'eng', config='-psm 10'))
print(np.median(img))

imshow("1", img)
imshow("2", morph)
imshow("3", bin)
waitKey(0)