from wxe_cmfz.settings import MENU_LIST, PERMISSION_LIST


def init_permission(user, request):
    # 用户存在代表登录成功，则获取当前登录用户的权限

    permission_url = user.roles.filter(permissions__isnull=False).values("permissions__url",
                                                                         "permissions__is_menu",
                                                                         "permissions__title",
                                                                         "permissions__category",
                                                                         "permissions__static_html",
                                                                         "permissions__id").distinct()

    # 用户可以访问的所用的权限
    # permission_list = [item['permissions__url'] for item in permission_url]

    # 用户权限中能够成为菜单的
    menu_list = []
    permission_list = []

    for url in permission_url:
        permission_list.append(url['permissions__url'])
        # 判断哪些是菜单的url  True是菜单
        if url['permissions__is_menu']:
            temp = {
                "title": url['permissions__title'],
                "url": url['permissions__url'],
                "id": url['permissions__id'],
                "static_html": url['permissions__static_html'],
                "category": url['permissions__category'],
            }
            menu_list.append(temp)
    print(MENU_LIST, menu_list)
    # 将权限列表存入session
    request.session[PERMISSION_LIST] = permission_list
    # 将菜单权限列表存入session
    request.session[MENU_LIST] = menu_list
