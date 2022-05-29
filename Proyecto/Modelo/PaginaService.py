import cv2
import numpy as np
import os.path
from PIL import Image


def analisis_pixel_BGR(path):
    with Image.open(path) as imgg:

        img = cv2.imread("Temp/" +os.path.basename(path))
        contB = 0
        for fila in range(imgg.height):
            for col in range(imgg.width):
                if img[fila, col][0] >= 230 and img[fila, col][1] >= 230 and img[fila, col][2] >= 230:
                    contB = contB + 1

        cont2 = contB / (imgg.width * imgg.height)

        coberturabco = cont2 * 100
        coberturacolor = 100 - coberturabco

        datospagina = [imgg.width, imgg.height, coberturacolor]
        print(datospagina)
        return datospagina
