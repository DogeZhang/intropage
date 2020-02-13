from keras.preprocessing import image
from keras.models import load_model
import os
import numpy as np

# 加载网络模型
net = load_model('resnet50_ship.h5')
# 检测类型
cls_list = ['bulk_carrier', 'container_ship', 'cruise_ship']
# 检测图片路径（文件夹）
img_path = '../static/predict'
# 检索待检测图片
files = os.listdir(img_path)

# 判断待检测图片是否唯一
if len(files) != 1:
    print("ResNet50/ResNetPredict--wrong: multiple files.")
else:
    # 判断是否为图片
    if files[0].endswith('jpg'):
        img = image.load_img(os.path.join(img_path, files[0]), target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        pred = net.predict(img)[0]
        predict_result = pred.argsort()[::-1][:5]
        print("input file predict result: " + files[0])
        for i in predict_result:
            print('    {:.3f}  {}'.format(predict_result[i], cls_list[i]))
    else:
        print("ResNet50/ResNetPredict--wrong: no jpg file.")
# for f in files:
#     if f.endswith('jpg'):
#         img = image.load_img(os.path.join(img_path, f), target_size=(224, 224))
#         if img is None:
#             continue
#         x = image.img_to_array(img)
#         x = np.expand_dims(x, axis = 0)
#         pred = net.predict(x)[0]
#         top_inds = pred.argsort()[::-1][:5]
#         print(f)
#         for i in top_inds:
#             print('    {:.3f}  {}'.format(pred[i], cls_list[i]))







