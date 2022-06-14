import os
from Modelo import Archivo
from Modelo.Config import Config
from Modelo.PaginaService import *
from Modelo.Pagina import *
from pathlib import Path
import pdf2image as pdf2image
from PIL import Image
from Modelo.Imagen import *


def entrada_archivo(path):
    config = Config()
    config.set_valores_iniciales()
    path = Path(path)
    try:
        #print("hola")
        if path.suffix == '.pdf':
            archivo = Archivo.Archivo()
            info = analizarpdf(path, archivo, config)
            return info
        else:
            try:
                #print("hola, hola")
                imagen = Imagen()
                info_imagen = analizarImagen(path, imagen, config)
                return info_imagen
            except IOError:
                mensajeError = ["Imagen no compatible"]
                return mensajeError
    except Exception as e:
        # imprimir en pantalla "formato no compatible"
        print(e)
        #print("algo")
    finally:
        # borrar los archivos en el directorio Temp
        path_list = Path(os.path.dirname(__file__).replace("Modelo", "Temp")).glob('**/*.*')
        for path in path_list:
            os.remove(path)

        #print(os.path.dirname(__file__).replace("Modelo", "Temp"))


def analizarpdf(PDFpath, archivo, config):
    images_from_path = pdf2image.convert_from_path(PDFpath, dpi=72, size=(595, None),
                                                   output_folder=os.path.dirname(__file__).replace("Modelo", "Temp"))
    # devuelve una lista con todos los archivos dentro del directorio
    pathlist = Path(os.path.dirname(__file__).replace("Modelo", "Temp")).glob('**/*.ppm')

    for path in pathlist:
        #print(path)
        # llamar al metodo de analisis de pixel enviando el path como source
        datospagina = analisis_pixel_BGR(path)
        #print(datospagina)
        pagina = Pagina(alto=datospagina[0], ancho=datospagina[1], cobertura=datospagina[2])
        #print(str(pagina))
        archivo.add_pagina(pagina)

    #print(str(archivo))
    archivo.calcular_precio_archivo(config)
    #print(getattr(archivo, 'precio'))
    info = [os.path.basename(PDFpath), len(archivo.paginas), getattr(archivo, 'precio')]
    #print(str(info))
    return info


def analizarImagen(ImgPath, imagen, config):
    # analisis pixel
    analisis_pixel_BGR_Imagen(imagen, ImgPath)

    # calculo de costo y precio
    imagen.calcular_precio_imagenA4(config)
    imagen.calcular_precio_imagenA5(config)
    info = [os.path.basename(ImgPath), "Precio imagen A4:", getattr(imagen, 'precioA4'), "Precio imagen A5:", getattr(imagen, 'precioA5')]
    #print(info)
    return info
