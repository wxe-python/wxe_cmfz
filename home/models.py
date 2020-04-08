from django.db import models


# Create your models here.
class Carousel(models.Model):  # 轮播图
    title = models.CharField(max_length=50)  # 标题
    status = models.SmallIntegerField()  # 状态
    create_time = models.DateField(auto_now_add=True)  # 创建时间
    pic = models.ImageField(upload_to='pics')  # 图片路径


class Admin(models.Model):    # 管理员表
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)   # 姓名
    password = models.CharField(max_length=20, blank=True, null=True)    # 密码
    phone = models.CharField(max_length=20, blank=True, null=True)  # 手机号码


# class User(models.Model):  # 用户表
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=20, blank=True, null=True)   # 用户名
#     phone = models.CharField(max_length=20, blank=True, null=True)     # 手机号码
#     password = models.CharField(max_length=20, blank=True, null=True)    # 密码
#     image = models.CharField(max_length=20, blank=True, null=True)     # 头像
#     address = models.CharField(max_length=20, blank=True, null=True)    # 所在地
#     signature = models.CharField(max_length=20, blank=True, null=True)    # 个人签名
#     sex = models.CharField(max_length=20, blank=True, null=True)    # 性别
#     number = models.CharField(max_length=20, blank=True, null=True)   # 盐
#     status = models.CharField(max_length=20, blank=True, null=True)   # 是否登陆状态
#     address_item = models.CharField(max_length=50, blank=True, null=True)   # 最近一次登录地址
#     regist_time = models.DateField(blank=True, null=True)   # 注册时间
#     email = models.CharField(max_length=20, blank=True, null=True)   # 邮箱
#
#     class Meta:
#         db_table = 't_user'
