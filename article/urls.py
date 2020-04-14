from django.urls import path
from article import views


app_name = 'article'
urlpatterns = [
    path('html/', views.html, name='html'),   # 页面渲染
    path('edit/', views.edit, name='edit'),    # 删除
    path('editt/', views.editt, name='editt'),    # 修改
    path('save/', views.save, name='save'),    # 保存
    path('upload_img/', views.upload_img, name='upload_img'),
    path('get_all_img/', views.get_all_img, name='get_all_img'),
   ]
