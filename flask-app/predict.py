import numpy as np
from cv2 import cv2
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model
from tensorflow.keras.applications import DenseNet121

from image_preprocessing import preprocess_img



class CovidCXR(object):
    OUTPUT_LIST = ['COVID', 'Fibrosis', 'Normal', 'PNEUMONIA', 'Tuberculosis']

    def __init__(self, model_weights_file, IMG_HEIGHT, IMG_WIDTH):
        self.IMG_HEIGHT = IMG_HEIGHT
        self.IMG_WIDTH = IMG_WIDTH
        base = DenseNet121(
            include_top=False,
            weights='imagenet',
            input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
            pooling='avg'
        )
        output = Dense(5, activation='softmax')(base.output)

        self.model = Model(inputs=base.input, outputs=output) 
        self.model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['binary_accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
        )

        self.model.load_weights(model_weights_file)
        
    def predict(self, img):
        img = cv2.imread("C:/Users/dell/3D Objects/Coronavirus X-ray project - Major/source code/flask-app/uploads/" + img)
        img = preprocess_img(img, self.IMG_HEIGHT, self.IMG_WIDTH)
        self.preds = self.model.predict(img)
        acc = str(int(np.amax(self.preds)*100)) + "%"
        return str(CovidCXR.OUTPUT_LIST[np.argmax(self.preds)]) + "-" + acc


