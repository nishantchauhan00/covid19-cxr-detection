from cv2 import cv2
import numpy as np


def preprocess_img(img, IMG_HEIGHT, IMG_WIDTH):
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation=cv2.INTER_AREA)
    img = np.array([img])
    return img

