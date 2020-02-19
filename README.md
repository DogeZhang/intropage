# intropage
This is a project for Ship Recognize.

## 目录
`backend/`  后端：运行`Django`与图像处理程序

`frontend/` 前端：`Vue.js`项目，执行交互任务

## 环境：
### CPU
 * python 3.6.5
 * Django 2.2.5
 * django-cors-headers 3.2.1
 * tensorflow 1.14.0
 * keras 2.2.5
 * numpy 1.16.4

### GPU
 * Windows 10
 * NVIDIA MX250
 * CUDA 10.0
 * cudnn v7.6.5.32
 * python 3.6.5
 * Django 2.2.5
 * django-cors-headers 3.2.1
 * tensorflow-gpu 2.0.0
 * Keras 2.3.0
 * numpy 1.18.1


> 因为小米笔记本显卡无法安装公版驱动的缘故 
> * CUDA 10.1及以上会出现不支持驱动报错
> * CUDA 9.2以下同样报错
> * CUDA 10.0能够运行
> * 目前尝试的Tensorflow-gpu最佳版本为2.0.0， Keras版本2.3.0
> 能够正常使用GPU运行网络。

> Django运行时无法正常调用Keras 2.3.0 报错：
```
AttributeError: '_thread._local' object has no attribute 'value'
```
> 因此Django会与Keras2.3.0发生冲突，无法同时运行。 Keras降级至2.2.5会与tensorflow-gpu冲突。
>
> 解决办法：在不使用Django的情况下，使用GPU训练，并保存网络模型。
> 在执行阶段使用CPU计算网络预测。

> **Django + tensorflow 1.14.0 + keras 2.2.5 运行正常**
>
> **建议安装tensorflow 1.14 版本与 Keras 2.2.5 版本**

## 安装

### 搭建环境

 * 运行环境
 * * 安装 Nodejs
 * * 安装 anaconda
 * * 创建虚拟环境：
 ```
conda create -n introPage python=3.6
conda activate introPage
pip install Django==2.2.5 django-cors-headers numpy==1.16.4 keras==2.2.5 tensorflow==1.14.0 pillow
 ```

如果下载速度较慢可以使用镜像源
```
pip install Django==2.2.5 django-cors-headers numpy==1.16.4 keras==2.2.5 tensorflow==1.14.0 pillow -i https://mirrors.aliyun.com/pypi/simple
```

 * 获取项目
 下载zip 或 运行指令：
```
git clone https://github.com/DogeZhang/intropage.git
cd intropage
```
 
 
### 前端

 * 进入 `frontend/`
 * 安装所需包
```
cd frontend
npm install
```
 * 运行
```
npm run dev
```
 * webpack 打包
```
npm run build
```
 * * 打包后进入`frontend/dist/index.html`
 
 ### 后端

 * 执行
 * 进入 `backend/`
```
python manage.py runserver
```
