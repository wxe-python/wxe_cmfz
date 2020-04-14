from django.urls import path

from rbac import views

app_name = "rbac"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("check_user/", views.check_user, name="check_user"),
]
