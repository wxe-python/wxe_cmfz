from django.urls import path
from banner import views
app_name = 'banner'
urlpatterns = [
    path('html/', views.html, name='html'),
    path('save/', views.save, name='save'),
    path('edit/', views.edit, name='edit'),
   ]
