from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission


def login(request):
    return render(request, "login_form.html")


def check_user(request):
    """
    用户登录的方法
    :param request:
    :return:
    """
    username = request.POST.get("name")
    pwd = request.POST.get('pwd')

    print(username, pwd)

    user = UserInfo.objects.filter(username=username, password=pwd).first()

    if not user:
        return render(request, "login_form.html", {'msg': "用户名或密码错误"})

    # 处理权限相关的业务
    init_permission(user, request)

    return redirect("/home/home/")

