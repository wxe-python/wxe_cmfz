import json
import os
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from home.models import Article, Pic


# 序列化
def my_default(a):
    if isinstance(a, Article):
        return {'id': a.id,
                'content': a.content,
                'title': a.title,
                'status': a.status,
                'createDate': str(a.create_date),
                'publishDate': str(a.publish_date),
                }


def html(request):  # 页面
    row = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pgtor = Paginator(Article.objects.all(), per_page=row)
    pg = pgtor.page(page)
    data = {
        'page': page,
        'total': pgtor.num_pages,
        'records': pgtor.count,
        'rows': list(pg)
    }
    json_str = json.dumps(data, default=my_default)
    return HttpResponse(json_str)


@csrf_exempt  # 解决csrf
def edit(request):   # 删除
    option = request.POST.get("oper")
    id = request.POST.get("id")
    if option == "del":
        Article.objects.get(pk=id).delete()
    return HttpResponse("success")


@xframe_options_sameorigin  # 允许页面嵌套时发起访问
@csrf_exempt
def upload_img(request):
    file = request.FILES.get("imgFile")
    if file:
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/img/" + str(file)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(img=file)
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_all_img(request):
    # 找到图片所在的目录  方便进行回显
    pic_dir = request.scheme + "://" + request.get_host() + '/'
    pic_list = Pic.objects.all()

    rows = []
    for i in list(pic_list):
        # 获取图片的后缀
        path, pic_suffix = os.path.splitext(i.img.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.img.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.img.name,
            "datetime": ""
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_dir,
        "total_count": len(pic_list),
        "file_list": rows

    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def save(request):  # 保存逻辑
    category = request.GET.get('category')  # 状态
    title = request.GET.get('title')
    content = request.GET.get('content')
    print(category, title, content)
    if category == '1':
        category = 1
    else:
        category = 0
    Article.objects.create(title=title, status=category, content=content)
    print(category, title, content)
    return HttpResponse("保存成功")

