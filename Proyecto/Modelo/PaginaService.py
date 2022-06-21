from tkinter import messagebox

import cv2
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
        return datospagina

def analisis_pixel_BGR_Imagen(imagen, path):
    with Image.open(path) as imgg:
        if imgg.width * imgg.height < 842 * 595:
            messagebox.showinfo(
                message="La resolución de la imagen es pequeña. No se ha ajustado a página para no perder calidad.",
                title="Atención")

        im1 = imgg
        #impresionA4
        if im1.width>im1.height:
            im1.thumbnail((842, 595))
            im1.save(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")
        else:
            im1.thumbnail((595, 842))
            im1.save(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")

        cantPixA4 = 842*595
        cantPixSobra = cantPixA4 - (im1.height*im1.width)
        porcentajePixBlancosHj = cantPixSobra*100/cantPixA4

        im = cv2.imread(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")

        #analisis pixel
        contB = 0
        for fila in range(im1.height):
            for col in range(im1.width):
                if im[fila, col][0] >= 230 and im[fila, col][1] >= 230 and im[fila, col][2] >= 230:
                    contB = contB + 1

        cont2 = contB / (im1.width * im1.height)

        coberturabco = cont2 * 100
        imagen.coberturaA4 = 100 - (coberturabco + porcentajePixBlancosHj)

        im2 = imgg
        #impresionA5
        if im2.height>im2.width:
            im2.thumbnail((420, 595))
            im2.save(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")
        else:
            im2.thumbnail((595, 420))
            im2.save(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")

        cantPixA4 = 842*595
        cantPixSobra = cantPixA4 - (im2.height*im2.width)
        porcentajePixBlancosHj2 = cantPixSobra*100/cantPixA4

        im = cv2.imread(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")

        #analisis pixel
        contB = 0
        for fila in range(im2.height):
            for col in range(im2.width):
                if im[fila, col][0] >= 230 and im[fila, col][1] >= 230 and im[fila, col][2] >= 230:
                    contB = contB + 1

        cont2 = contB / (im2.width * im2.height)

        coberturabco2 = cont2 * 100
        imagen.coberturaA5 = 100 - (coberturabco2 + porcentajePixBlancosHj2)
