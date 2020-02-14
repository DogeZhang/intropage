# intropage
This is a project for Ship Recognize.

## 目录
`backend/`  后端：运行`Django`与图像处理程序

`frontend/` 前端：`Vue.js`项目，执行交互任务

## 环境：
### CPU
* python 3.6.5
* Django 2.2.5
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
```angular2
AttributeError: '_thread._local' object has no attribute 'value'
```
> Keras降级至2.2.5会与tensorflow-gpu冲突。
 
> Django + tensorflow 1.14.0 + keras 2.2.5 运行正常