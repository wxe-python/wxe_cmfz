import json

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from home.models import Carousel


# 序列化
def my_default(a):
    if isinstance(a, Carousel):
        return {'id': a.id,
                'title': a.title,
                'status': a.status,
                'create_time': str(a.create_time),
                'pic': str(a.pic)}


def html(request):
    row = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pgtor = Paginator(Carousel.objects.all(), per_page=row)
    pg = pgtor.page(page)
    data = {
        'page': page,
        'total': pgtor.num_pages,
        'records': pgtor.count,
        'rows': list(pg)
    }
    json_str = json.dumps(data, default=my_default)
    return HttpResponse(json_str)


@csrf_exempt
def save(request):
    try:
        title = request.POST.get('title')
        status = request.POST.get('status')
        pic = request.FILES.get('pic')
        print(title, status, pic)
        if not pic:
            return HttpResponse("图片不能为空")
        with transaction.atomic():  # 事务回滚
            Carousel.objects.create(title=title, status=status, pic=pic)
        return HttpResponse('成功保存')
    except:
        return HttpResponse('保存失败')


@csrf_exempt  # 解决csrf
def edit(request):
    option = request.POST.get("oper")
    if option == "edit":  # 修改
        id = request.POST.get('id')
        title = request.POST.get('title')
        status = request.POST.get('status')

        car = Carousel.objects.get(id=id)
        car.title = title
        car.status = status
        car.save()

    elif option == "del":  # 删除
        id = request.POST.get("id")
        Carousel.objects.get(pk=id).delete()

    return HttpResponse("success")
