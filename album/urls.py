from django.urls import path
from album import views

app_name = 'album'
urlpatterns = [
    path('html/', views.html, name='html'),  # 一级列表
    path('edit/', views.edit, name='edit'),  # 增删改
    path('html2/', views.html2, name='html2'),  # 二级列表
    path('editt/', views.editt, name='editt'),  # 增删改
    path('save/', views.save, name='save'),  # 添加
    path('dell/', views.dell, name='dell'),  # 删除
]
