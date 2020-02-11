import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backend.ImageProcessor.ProcessImage import *
from intropage.settings import BASE_DIR


file_path = BASE_DIR + "\\backend\\static\\img\\"


def upload_image(request):
    # 从前端得到图片并保存
    if request.method == 'GET':
        return render(request, 'not support GET method')
    else:
        # 清空服务器缓存图片
        for i in os.listdir(file_path):
            os.remove(file_path + "\\" + i)
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
        img = open(file_path + file_name, 'rb')
        imagedata = img.read()
        return HttpResponse(imagedata, content_type="image/png")
    except Exception as e:
        print(e)
        return HttpResponse("the " + file_name + " does not exist.")
