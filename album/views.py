import json
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mutagen.mp3 import MP3
from home.models import Album, Chapter


# 第一层列表
def my_default(u):
    if isinstance(u, Album):
        return {
            "author": u.author,
            "brief": u.brief,
            "broadcast": u.broadcast,
            "count": u.count,
            "cover": str(u.cover),
            "createDate": u.create_date.strftime('%Y-%m-%d'),
            "id": u.id,
            "publishDate": u.publish_date.strftime('%Y-%m-%d'),
            "score": u.score,
            "status": u.status,
            "title": u.title,
        }


def html(request):
    page = request.GET.get('page', 1)
    row = request.GET.get('rows')
    album = Album.objects.all().order_by('id')
    all_page = Paginator(album, row)
    page_num = all_page.num_pages  # 获取总页面数
    if int(page) > page_num:
        page = page_num
    page_obj = all_page.page(page).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_obj),
    }
    data = json.dumps(page_data, default=my_default)
    return HttpResponse(data)


@csrf_exempt
def edit(request):
    option = request.POST.get("oper")
    id = request.POST.get('id')
    if option == "add":  # 增
        title = request.POST.get('title')
        status = request.POST.get('status')
        author = request.POST.get('author')
        brief = request.POST.get('brief')
        broadcast = request.POST.get('broadcast')
        count = request.POST.get('count')
        create_date = request.POST.get('createDate')
        publish_date = request.POST.get('publishDate')
        score = request.POST.get('score')
        cover = request.FILES.get('cover')
        Album.objects.create(title=title, status=status, author=author,
                             brief=brief, broadcast=broadcast, count=count,
                             cover=cover, create_date=create_date,
                             publish_date=publish_date, score=score)

    elif option == "edit":  # 修改
        title = request.POST.get('title')
        status = request.POST.get('status')
        author = request.POST.get('author')
        brief = request.POST.get('brief')
        broadcast = request.POST.get('broadcast')
        count = request.POST.get('count')
        cover = request.POST.get('cover')
        create_date = request.POST.get('createDate')
        publish_date = request.POST.get('publishDate')
        score = request.POST.get('score')
        alb = Album.objects.get(pk=int(id))
        alb.title = title
        alb.status = status
        alb.author = author
        alb.brief = brief
        alb.broadcast = broadcast
        alb.count = count
        alb.cover = cover
        alb.create_date = create_date
        alb.publish_date = publish_date
        alb.score = score
        alb.save()

    elif option == "del":  # 删除
        Album.objects.get(pk=int(id)).delete()

    return HttpResponse("success")


# 第二层列表
def mydefault(u):
    if isinstance(u, Chapter):
        return {
            "albumId": u.album_id,
            "createDate": u.create_date,
            "duration": u.time_long,
            "id": u.id,
            "size": u.size,
            "title": u.title,
            "status": u.status,
            "url": u.url,
        }


def html2(request):
    row = request.GET.get('rows')
    page = request.GET.get('page', 1)
    album_Id = request.GET.get('albumId')
    album = Chapter.objects.all().filter(album_id=album_Id).order_by('id')
    all_page = Paginator(album, row)
    page_num = all_page.num_pages  # 获取总页面数
    if int(page) > page_num:
        page = page_num
    page_obj = all_page.page(page).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_obj),
    }
    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@csrf_exempt
def editt(request):
    option = request.POST.get("oper")
    id = request.POST.get('id')
    if option == "edit":  # 改
        title = request.POST.get('title')
        status = request.POST.get('status')
        chapter = Chapter.objects.get(pk=id)
        chapter.title = title
        chapter.status = status
        chapter.save()
    elif option == "del":  # 删
        chapter = Chapter.objects.get(pk=id)
        chapter.delete()
    return HttpResponse("success")


@csrf_exempt
def save(request):
    album_id = request.POST.get("album_id")
    title = request.POST.get("title")
    audio = request.FILES.get("audio")
    status = request.POST.get("status")
    print(title, status, audio)
    size = str(round(audio.size / 2 ** 20, 2)) + 'MB'    # 音频大小
    audio_mp3 = MP3(audio)  # 音频时长
    time_long = str(round(audio_mp3.info.length / 60, 2)) + "分"
    album = Album.objects.get(pk=int(album_id))
    Chapter.objects.create(album_id=album, title=title, url=audio, status=status, size=size,
                           time_long=time_long, audio=audio)
    return HttpResponse("success")


def dell(request):
    id = request.GET.get('id')
    Chapter.objects.get(pk=int(id)).delete()
    return HttpResponse("success")
