import os.path

import cv2
from matplotlib import pyplot as plt
from PIL import Image

def histograma(path):

    img = cv2.imread(os.path.dirname(__file__).replace("Modelo", "Temp") + "/Img.jpeg")
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # print('Reescalado: ', resized.shape)
    # cv2.imshow("Reescalado 60%", resized)

    color = ('b', 'g', 'r')

    for i, c in enumerate(color):
        hist = cv2.calcHist([resized], [i], None, [256], [0, 256])
        plt.plot(hist, color=c)
        plt.xlim([0, 256])

    plt.show()
    cv2.waitKey(0)



