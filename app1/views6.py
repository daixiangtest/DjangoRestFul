from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import generics

"""
视图集类的使用： ModelViewSet
    ViewSet视图集类不再实现get()、post()等方法，而是实现动作 action 如 list() 、create() 等。将一系列逻辑相关的动作放到一个类中：
    list() 提供一组数据
    retrieve() 提供单个数据
    create() 创建数据
    update() 保存数据
    destory() 删除数据
    使用视图集类值需要继承视图集方法，在urls.py中的路由配置对应的方法即可如下示例：
    urlpatterns = [
        path(r'^books/$', XXViewSet.as_view({'get':'list'}),
        path(r'^books/<int:id>/$', XXXnfoViewSet.as_view({'get': 'retrieve'})
        ]


"""


# DRF的视图函数
class UserList(ModelViewSet):
    # 继承ModelViewSet后，对数据表的增删改查直接通过路由来指定即可
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01
