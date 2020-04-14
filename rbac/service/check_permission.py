import re

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from sj_cmfz.settings import MENU_LIST, PERMISSION_LIST

class CheckPermission(MiddlewareMixin):
    """
    用户权限信息的校验
    """

    def process_request(self, request):
        """
        当用户重定向到首页之前执行此方法
        :param request:
        当前用户访问url
        获取用户的权限列表
        权限匹配
        :return: 是否有权限
        """

        # 对于不需要拦截的url设置白名单
        valid_url_list = [
            '/rbac/login/',
            '/rbac/check_user/',
            '/admin/.*',
        ]

        # 当前访问的url
        current_url = request.path_info
        # 权限列表
        per_list = request.session.get(PERMISSION_LIST)

        for url in valid_url_list:
            if re.match(url, current_url):
                return None

        if not per_list:
            return redirect("/rbac/login/")

        # 需要使用正则来进行匹配
        for url in per_list:
            if re.match(url, current_url):
                return None

        return HttpResponse("无权访问")
