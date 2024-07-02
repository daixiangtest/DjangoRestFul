from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

"""
视图扩展类：mixins继承了GenericAPIView类主要实现一些通用的查询方法
    ListModelMixin：列表视图扩展类，提供`list方法快速实现列表视图
    CreateModelMixin ：创建视图扩展类，提供create方法快速实现创建资源的视图
"""


# DRF的视图函数
class UserList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetaill(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
