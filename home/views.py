import re

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from utils import random_code
from wxe_cmfz.settings import API_KEY
from utils.send_mess import YunPian

from redis import Redis

redis = Redis(host='localhost', port=6379)  # 连接redis数据库


def home(request):     # 首页
    return render(request, 'home.html')


def login(request):     # 登录页面
    return render(request, 'login.html')


@csrf_exempt
def get_code(request):    # 登录页面发送验证码按钮
    mobile = request.POST.get("mobile")
    res = redis.get(mobile)
    if res:
        return HttpResponse("频繁发送")
    ret = re.match(r"^((13[0-9])|(14[5-9])|(15[0-3])|(15[5-9])|(166)|(17[0-8])|(18[0-9])|(19[8-9]))\d{8}$", mobile)
    print(ret, 1111)
    if ret:
        yun_pian = YunPian(API_KEY)
        yun_pian.send_message(mobile, random_code.a)
        redis.setex(mobile, 60, random_code.a)
        return HttpResponse("success")
    else:
        return HttpResponse('手机号格式不正确')


@csrf_exempt
def check_user(request):    # 登录成功逻辑
    mobile = request.GET.get('mobile')
    name = request.GET.get("name")
    code = request.GET.get('code')
    print(mobile, name, code)
    res = redis.get(mobile)
    if res:
        request.session['mobile'] = mobile
        return HttpResponse('成功')
    return HttpResponse('输入错误')