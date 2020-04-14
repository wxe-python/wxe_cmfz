from django.db import models


# Create your models here.

class Permission(models.Model):
    title = models.CharField(verbose_name="标题", max_length=200)
    url = models.CharField(verbose_name="含正则的URL", max_length=200)
    static_html = models.CharField(verbose_name="要加载html", max_length=200, null=True,default=None)
    is_menu = models.BooleanField(verbose_name="是否是菜单", default=False)
    category = models.CharField(verbose_name="所属模块", max_length=200, null=True,default=None)

    def __str__(self):
        return self.title


class Role(models.Model):
    role = models.CharField(verbose_name="角色名称", max_length=200)
    permissions = models.ManyToManyField(verbose_name="拥有的所有权限", to="Permission", blank=True)

    def __str__(self):
        return self.role


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=200)
    password = models.CharField(verbose_name="密码", max_length=200)
    email = models.CharField(verbose_name="邮箱", max_length=200)
    roles = models.ManyToManyField(verbose_name="拥有的所有角色", to="Role", blank=True)

    def __str__(self):
        return self.username
