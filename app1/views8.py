from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserInfoFilter
from app1.pagination import StuPagination

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
    # 访问权限只有登录用户才可以访问
    permission_classes = (IsAuthenticated,)
    # 不是登录用户只能访问get方法
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    # 继承ModelViewSet后，对数据表的增删改查直接通过路由来指定即可
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01
    # 指定默认的过滤器类
    # filterset_fields = ('age',)
    # 指定自定义的过滤器
    filterset_class = UserInfoFilter
    # 指定需要排序的字段
    ordering_fields = ('age', 'id')
    # url 指明通过age字段排序
    # 127.0.0.1:8000/students/?ordering=age
    # url 指明通过id字段排序
    # 127.0.0.1:8000/students/?ordering=id
    # 开启分页功能
    pagination_class = StuPagination
