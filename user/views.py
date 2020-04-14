from home.models import User
import json
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
import datetime

from redis import Redis

redis = Redis(host='localhost', port=6379)  # 连接redis数据库


def my_default(e):
    if isinstance(e, User):
        h = hashlib.sha256()
        h.update(e.password.encode())
        password1 = h.hexdigest()
        if e.status == "1":
            return {'id': e.id,
                    "username": e.username,
                    "sex": e.sex,
                    "phone": e.phone,
                    "password": password1,
                    "image": str(e.image),
                    "address": e.address,
                    "address_item": e.address_item,
                    "signature": e.signature,
                    "regist_time": str(e.regist_time),
                    "status": "正常"}
        return {'id': e.id,
                "username": e.username,
                "sex": e.sex,
                "phone": e.phone,
                "password": password1,
                "image": str(e.image),
                "address": e.address,
                "address_item": e.address_item,
                "signature": e.signature,
                "regist_time": str(e.regist_time),
                "status": "冻结"}


def html(request):
    row = request.GET.get('rows')
    pagenum = request.GET.get('page', 1)
    pgtor = Paginator(User.objects.all(), per_page=row)
    page_num = pgtor.num_pages  # 获取总页面数
    # 判断获取的当前页数是否大于总页数，如果大于总页数则将总页数赋值给当前页数
    if int(pagenum) > page_num:
        pagenum = page_num
    page_obj = Paginator(User.objects.all(), row).page(pagenum).object_list
    data = {
        'page': pagenum,
        'total': pgtor.num_pages,
        'records': pgtor.count,
        'rows': list(page_obj)
    }
    json_str = json.dumps(data, default=my_default)
    return HttpResponse(json_str)


@csrf_exempt  # 解决csrf
def edit(request):
    id = request.POST.get('id')
    option = request.POST.get("oper")
    if option == "edit":  # 修改
        status = request.POST.get('status')
        car = User.objects.get(id=id)
        car.status = status
        car.save()

    elif option == "del":  # 删除
        User.objects.get(pk=id).delete()

    return HttpResponse("success")


def map(request):  # 中国地图
    data = redis.get("data2")
    if data:
        data = eval(data.decode())
        return JsonResponse(data, safe=False)
        # 通过用户的地区字段进行查询并求数量   地区必须直辖市或者省
    c1 = User.objects.filter(address="北京").count()
    c2 = User.objects.filter(address="天津").count()
    c3 = User.objects.filter(address="上海").count()
    c4 = User.objects.filter(address="重庆").count()
    c5 = User.objects.filter(address="河北").count()
    c6 = User.objects.filter(address="河南").count()
    c7 = User.objects.filter(address="云南").count()
    c8 = User.objects.filter(address="辽宁").count()
    c9 = User.objects.filter(address="湖南").count()
    c10 = User.objects.filter(address="安徽").count()
    c11 = User.objects.filter(address="山东").count()
    c12 = User.objects.filter(address="新疆").count()
    c13 = User.objects.filter(address="江苏").count()
    c14 = User.objects.filter(address="浙江").count()
    c15 = User.objects.filter(address="江西").count()
    c16 = User.objects.filter(address="湖北").count()
    c17 = User.objects.filter(address="广西").count()
    c18 = User.objects.filter(address="甘肃").count()
    c19 = User.objects.filter(address="山西").count()
    c20 = User.objects.filter(address="陕西").count()
    c21 = User.objects.filter(address="吉林").count()
    c22 = User.objects.filter(address="福建").count()
    c23 = User.objects.filter(address="贵州").count()
    c24 = User.objects.filter(address="广东").count()
    c25 = User.objects.filter(address="青海").count()
    c26 = User.objects.filter(address="西藏").count()
    c27 = User.objects.filter(address="四川").count()
    c28 = User.objects.filter(address="宁夏").count()
    c29 = User.objects.filter(address="海南").count()
    c30 = User.objects.filter(address="台湾").count()
    c31 = User.objects.filter(address="香港").count()
    c32 = User.objects.filter(address="澳门").count()
    c33 = User.objects.filter(address="黑龙江").count()
    c34 = User.objects.filter(address="内蒙古").count()
    data = [
        {"name": '北京', "value": c1},
        {"name": '天津', "value": c2},
        {"name": '上海', "value": c3},
        {"name": '重庆', "value": c4},
        {"name": '河北', "value": c5},
        {"name": '河南', "value": c6},
        {"name": '云南', "value": c7},
        {"name": '辽宁', "value": c8},
        {"name": '湖南', "value": c9},
        {"name": '安徽', "value": c10},
        {"name": '山东', "value": c11},
        {"name": '新疆', "value": c12},
        {"name": '江苏', "value": c13},
        {"name": '浙江', "value": c14},
        {"name": '江西', "value": c15},
        {"name": '湖北', "value": c16},
        {"name": '广西', "value": c17},
        {"name": '甘肃', "value": c18},
        {"name": '山西', "value": c19},
        {"name": '陕西', "value": c20},
        {"name": '吉林', "value": c21},
        {"name": '福建', "value": c22},
        {"name": '贵州', "value": c23},
        {"name": '广东', "value": c24},
        {"name": '青海', "value": c25},
        {"name": '西藏', "value": c26},
        {"name": '四川', "value": c27},
        {"name": '宁夏', "value": c28},
        {"name": '海南', "value": c29},
        {"name": '台湾', "value": c30},
        {"name": '香港', "value": c31},
        {"name": '澳门', "value": c32},
        {"name": '黑龙江', "value": c33},
        {"name": '内蒙古', "value": c34},
    ]
    redis.setex("data2", 24 * 3600, str(data))
    return JsonResponse(data, safe=False)


def echarts(request):  # 注册趋势图
    data1 = redis.get("data1")
    if data1:
        data = eval(data1.decode())
        return JsonResponse(data, safe=False)
    # 当前日期
    now = datetime.datetime.now().date()
    day01 = now - datetime.timedelta(days=1)
    day02 = now - datetime.timedelta(days=2)
    day03 = now - datetime.timedelta(days=3)
    day04 = now - datetime.timedelta(days=4)
    day05 = now - datetime.timedelta(days=5)
    day06 = now - datetime.timedelta(days=6)

    count1 = User.objects.filter(regist_time__gte=now).count()
    count2 = User.objects.filter(regist_time__gte=day01).count()
    count3 = User.objects.filter(regist_time__gte=day02).count()
    count4 = User.objects.filter(regist_time__gte=day03).count()
    count5 = User.objects.filter(regist_time__gte=day04).count()
    count6 = User.objects.filter(regist_time__gte=day04).count()
    count7 = User.objects.filter(regist_time__gte=day04).count()
    data = {
        "x": [str(now), str(day01), str(day02), str(day03), str(day04), str(day05), str(day06)],
        "y": [count1, count2, count3, count4, count5, count6, count7]
    }
    redis.setex("data1", 24 * 3600, str(data))
    return JsonResponse(data)
