import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from backend import predict
from backend.ImageProcessor.ProcessImage import ProcessImage

from intropage.settings import BASE_DIR
from keras.preprocessing import image


file_path = BASE_DIR + "\\backend\\static\\img\\"
example_path = BASE_DIR + "\\backend\\static\\example\\"

img_path = os.path.join(BASE_DIR, 'backend', 'static', 'img', 'predict')
# 检索待检测图片
files = os.listdir(img_path.replace("\\", '/'))
# 判断待检测图片是否唯一
if len(files) != 1:
    print("ResNet50/ResNetPredict--wrong: multiple files.")
else:
    # 判断是否为图片
    if files[0].endswith('jpg'):
        path = os.path.join(img_path, files[0])
        img = image.load_img(path.replace("\\", '/'), target_size=(224, 224))
        img = image.img_to_array(img)
        pred = predict(img)
        print("input file predict result: " + files[0])
        print(pred)
    else:
        print("ResNet50/ResNetPredict--wrong: no jpg file.")


def upload_image(request):
    # 从前端得到图片并保存
    if request.method == 'GET':
        return HttpResponse(request, 'not support GET method')
    else:
        # 清空服务器缓存图片
        for i in os.listdir(file_path):
            if i.endswith('jpg'):
                os.remove(os.path.join(file_path, i))
            else:
                for j in os.listdir(os.path.join(file_path, i)):
                    os.remove(os.path.join(file_path, i, j))
        # 接收前端的照片
        file_obj = request.FILES.get('file')
        print(request.FILES)
        file_name = file_obj.name
        # 将图片写入服务器端
        try:
            with open(file_path + file_name, 'wb') as img:
                for c in file_obj.chunks():
                    img.write(c)
        except Exception as e:
            print(e)
        print(file_name)
        # 使用ImageProcessor处理图片，生成原图+轮廓图+混合图
        processor = ProcessImage(file_path, file_name)
        processor.exec()
        images = {"original": processor.filePaths[0], "outline": processor.filePaths[1],
                  "original_outline": processor.filePaths[2]}
        return JsonResponse(images)


def get_image(request, file_name):
    try:
        if file_name == "EXAMPLE.jpg" or file_name == "d_EXAMPLE.jpg" or file_name == "o_EXAMPLE.jpg":
            img = open(example_path + file_name, 'rb')
        else:
            img = open(file_path + file_name, 'rb')
        imagedata = img.read()
        return HttpResponse(imagedata, content_type="image/png")
    except Exception as e:
        print(e)
        return HttpResponse("the " + file_name + " does not exist.")


def predict_image(request):
    predict_result = {}
    img_path = os.path.join(BASE_DIR, 'backend', 'static', 'img', 'predict')
    # 检索待检测图片
    files = os.listdir(img_path.replace("\\", '/'))
    # 判断待检测图片是否唯一
    if len(files) != 1:
        print("ResNet50/ResNetPredict--wrong: multiple files.")
    else:
        # 判断是否为图片
        if files[0].endswith('jpg'):
            path = os.path.join(img_path, files[0])
            img = image.load_img(path.replace("\\", '/'), target_size=(224, 224))
            img = image.img_to_array(img)
            pred = predict(img)
            print("input file predict result: " + files[0])
            pred[0] = round(pred[0], 2) * 100
            pred[1] = round(pred[1], 2) * 100
            pred[2] = round(pred[2], 2) * 100
            print(pred)
            predict_result = {
                "bulk": int(pred[0]),
                "container": int(pred[1]),
                "cruise": int(pred[2])
            }
        else:
            print("ResNet50/ResNetPredict--wrong: no jpg file.")
    return JsonResponse(predict_result)


