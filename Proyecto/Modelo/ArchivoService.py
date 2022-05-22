import tempfile
from pathlib import Path
import pdf2image as pdf2image

#no crea el archivo temporal, revisar
#crearlo en la carpeta del archivo
with tempfile.TemporaryDirectory(dir=r'../../../../../../../../../Desktop/PDF/') as tempdir:
    print(tempdir)
    images_from_path = pdf2image.convert_from_path(r'../../../../../../../../../Desktop/PDF/mementopython3-espanol.pdf',
                                                   output_folder=r'../../../../../../../../../Desktop/PDF/')

    #devuelve una lista con todos los archivos dentro del directorio
    pathlist = Path(r'../../../../../../../../../Desktop/PDF/').glob('**/*.ppm')
    for path in pathlist:
        print(path)

#borrar el directorio temporal después de usarlo
