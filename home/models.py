from django.db import models


# Create your models here.
class Carousel(models.Model):  # 轮播图
    title = models.CharField(max_length=50)  # 标题
    status = models.SmallIntegerField()  # 状态
    create_time = models.DateField(auto_now_add=True)  # 创建时间
    pic = models.ImageField(upload_to='pics')  # 图片路径


class Admin(models.Model):  # 管理员表
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)  # 姓名
    password = models.CharField(max_length=20, blank=True, null=True)  # 密码
    phone = models.CharField(max_length=20, blank=True, null=True)  # 手机号码


class User(models.Model):  # 用户表
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)  # 用户名
    sex = models.CharField(max_length=20, blank=True, null=True)  # 性别
    phone = models.CharField(max_length=20, blank=True, null=True)  # 手机号码
    password = models.CharField(max_length=20, blank=True, null=True)  # 密码
    image = models.CharField(max_length=20, blank=True, null=True)  # 头像
    address = models.CharField(max_length=20, blank=True, null=True)  # 地址
    address_item = models.CharField(max_length=50, blank=True, null=True)  # 详细地址
    signature = models.CharField(max_length=20, blank=True, null=True)  # 个人签名
    regist_time = models.DateField(auto_now_add=True)  # 注册时间
    status = models.CharField(max_length=20, blank=True, null=True)  # 状态

    class Meta:
        db_table = 't_user'


class Article(models.Model):
    id = models.IntegerField(primary_key=True)   # 编号
    title = models.CharField(max_length=255, blank=True, null=True)   # 标题
    content = models.TextField(blank=True, null=True)      # 内容
    create_date = models.DateField(auto_now_add=True)   # 上传时间
    publish_date = models.DateField(auto_now_add=True)   # 发布时间
    status = models.CharField(max_length=20, blank=True, null=True)  # 状态

    class Meta:
        db_table = 'article'


class Pic(models.Model):
    img = models.ImageField(upload_to='static/img')

    class Meta:
        db_table = 't_pic'
