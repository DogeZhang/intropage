from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class ProcessImage:
    filePath = ''
    fileName = ''
    filePaths = []

    dimension = 128
    different = 16

    def __init__(self, p, n):
        self.filePath = p
        self.fileName = n

    def exec(self):
        # 清空文件路径
        self.filePaths = []
        print(self.filePath + self.fileName)
        self.filePaths.append(self.fileName)
        img = np.array(Image.open(self.filePath + self.fileName))
        #self.reduce_dimension(img)
        #self.get_outline_with_reduce(img)
        self.get_outline_with_rgb(img)
        d_output = np.array(Image.open(self.filePath + "d_" + self.fileName))
        img = np.array(Image.open(self.filePath + self.fileName))
        self.generate_image_with_outline(img, d_output)


    # 色彩降阶
    def reduce_dimension(self, original):
        img = original
        [width, height, dim] = img.shape
        for j in range(0, height):
            for i in range(0, width):
                # 像素值
                r = img[i, j, 0]
                g = img[i, j, 1]
                b = img[i, j, 2]

                r = (r // self.dimension) * self.dimension
                g = (g // self.dimension) * self.dimension
                b = (b // self.dimension) * self.dimension
                # r = 0;
                # g = 0;
                # b = 0;

                img[i, j, 0] = r
                img[i, j, 1] = g
                img[i, j, 2] = b
        output = Image.fromarray(img.astype('uint8')).convert('RGB')
        output.save(self.filePath + "reduce_" + self.fileName)
        print("经过色彩降阶后的图像：" + self.filePath + "reduce_" + self.fileName)

    # 依照色彩降阶结果进行绘制轮廓
    def get_outline_with_reduce(self, original):
        img = original
        [width, height, dim] = img.shape
        for j in range(0, height - 1):
            for i in range(0, width - 1):
                # 像素值
                p = img[i, j]
                # 右侧像素
                right = img[i + 1, j]
                # 下方像素
                down = img[i, j + 1]

                if all(p == right) and all(p == down):
                    img[i, j] = [255, 255, 255]
                else:
                    img[i, j] = [0, 0, 0]
            img[i, j] = img[i - 1, j]
        output = Image.fromarray(img.astype('uint8')).convert('RGB')
        output.save(self.filePath + "r_" + self.fileName)
        print("依照色彩降阶结果进行绘制轮廓: " + self.filePath + "r_" + self.fileName)

    # 依照RGB差异绘制轮廓
    def get_outline_with_rgb(self, original):
        img = original
        [width, height, dim] = img.shape
        for j in range(0, height - 1):
            for i in range(0, width - 1):
                # 像素值
                p_R = int(img[i, j, 0])
                p_G = int(img[i, j, 1])
                p_B = int(img[i, j, 2])
                # 右侧像素
                right_R = int(img[i + 1, j, 0])
                right_G = int(img[i + 1, j, 1])
                right_B = int(img[i + 1, j, 2])
                # 下方像素
                down_R = int(img[i, j + 1, 0])
                down_G = int(img[i, j + 1, 1])
                down_B = int(img[i, j + 1, 2])
                if abs(p_R - right_R) < self.different and abs(p_G - right_G) < self.different and abs(
                        p_B - right_B) < self.different and abs(p_R - down_R) < self.different and abs(
                        p_G - down_G) < self.different and abs(p_B - down_B) < self.different:
                    img[i, j] = [255, 255, 255]
                else:
                    img[i, j] = [0, 0, 0]
            img[i, j] = img[i - 1, j]
        output = Image.fromarray(img.astype('uint8')).convert('RGB')
        output.save(self.filePath + "d_" + self.fileName)
        self.filePaths.append("d_" + self.fileName)
        print("依照RGB差异绘制轮廓: " + self.filePath + "d_" + self.fileName)

    # 将轮廓加入至原始图片中
    def generate_image_with_outline(self, original, d_output):
        img = original
        [width, height, dim] = img.shape
        for j in range(0, height - 1):
            for i in range(0, width - 1):
                if all(d_output[i, j] == [0, 0, 0]):
                    img[i, j] = [0, 0, 0]
        output = Image.fromarray(img.astype('uint8')).convert('RGB')
        output.save(self.filePath + "o_" + self.fileName)
        self.filePaths.append("o_" + self.fileName)
        print("将轮廓加入至原始图片中: " + self.filePath + "o_" + self.fileName)

