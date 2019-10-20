from django.contrib import admin
from django.urls import path,include
from home import views
# import home
urlpatterns = [
    # path('',include(login.urls)),
    path('test/', views.test),
    path('my_data/',views.mydate),#我的信息
    path('query_results/',views.query),#查询报告信息
    path('cet_4/',views.cet_4),#四级报名
    path('cet_6/',views.cet_6),#六级报名
    path('change_my_data/',views.updata),
]