import os

from Modelo.Archivo import Archivo
from Modelo.PaginaService import *
from Modelo.Pagina import *
from pathlib import Path
import pdf2image as pdf2image

def entrada_archivo(path):
    PDFpath = Path(path)
    try:
        print("hola")
        if PDFpath.suffix == '.pdf':
            archivo = Archivo()
            leerpdf(PDFpath)
    # else:
    #     if path tiene extension de archivo de imagen
    #         seleccion dimension de imagen en A4
    except Exception as e:
        #imprimir en pantalla "formato no compatible"
        print(e)
        print("algo")
    finally:
        #borrar los archivos en el directorio Temp
        path_list = Path(r"/Users/sebastiansulia/Documents/Tecnicatura_programacion/Semestre2/Metodología/Proyecto/Repos/GrupoD-TT/Proyecto/Temp").glob('**/*.ppm')
        for path in path_list:
            os.remove(path)

        print("final")

def leerpdf(PDFpath):
    images_from_path = pdf2image.convert_from_path(PDFpath,
                                                   output_folder=r"/Users/sebastiansulia/Documents/Tecnicatura_programacion/Semestre2/Metodología/Proyecto/Repos/GrupoD-TT/Proyecto/Temp")
    # devuelve una lista con todos los archivos dentro del directorio
    pathlist = Path(r"/Users/sebastiansulia/Documents/Tecnicatura_programacion/Semestre2/Metodología/Proyecto/Repos/GrupoD-TT/Proyecto/Temp").glob('**/*.ppm')
    for path in pathlist:
        print(path)
        #llamar al metodo de analisis de pixel enviando el path como source
        #datospagina = \
        analisis_pixel_BGR(path)
        #print(datospagina)
        #Archivo.add_pagina(Pagina(datospagina[0],datospagina[1],datospagina[2]))
