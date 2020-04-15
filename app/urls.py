from django.urls import path

from app import views

urlpatterns = [
    path("first_page/", views.first_page),
    path("album/", views.album),
    path("register/", views.register),
    path("modify/", views.modify),
]