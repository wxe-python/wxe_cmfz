from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('html/', views.html, name="html"),
    path('edit/', views.edit, name="edit"),
    path('map/', views.map, name="map"),
    path('echarts/', views.echarts, name="echarts"),
]
