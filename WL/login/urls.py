from django.contrib import admin
from django.urls import path,include
from login import views
# import home


urlpatterns = [
    # path('',include(login.urls)),
    path('', views.index),              # 修改端口默认主页
    path('check/', views.check),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('order_get/', views.order_get),
]
