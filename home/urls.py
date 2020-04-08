from django.urls import path
from home import views
app_name = 'home'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('get_code/', views.get_code, name='get_code'),
    path('check_user/', views.check_user, name='check_user'),
]
