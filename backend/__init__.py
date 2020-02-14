import os

from keras.models import load_model
import numpy as np

print('load model...')
# print(os.path.realpath(__file__))
# print(os.path.split(os.path.realpath(__file__))[0])
model = load_model(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'resnet50_ship.h5'), compile=False)
print('load done.')

print('test model...')
# 根据自己传入图片格式定义np.zeros（）
print(model.predict(np.zeros((2, 224, 224, 3))))
print('test done.')


def predict(img):
    global model
    result_vec = None
    img = np.expand_dims(img, axis=0)
    result_vec = model.predict(img)[0]
    return result_vec