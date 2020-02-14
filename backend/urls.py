from django.urls import path

from . import views


urlpatterns = [
    path('predict/', views.predict_image, name='predict_image'),
    path('<str:file_name>', views.get_image, name="get_image"),
    path('', views.upload_image, name='upload_image'),
]