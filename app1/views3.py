from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

"""
GenericAPIViewrest_framework.generics.GenericAPIView 继承自 APIVIew ，增加了对于列表视图和详情视图可能用到的通用支持方法。

扩展了类属性：queryset：  指定当前类视图使用的查询集
            serializer_class ：   类视图使用的序列化器
            新增以下方法来
            self.get_queryset():获取查询集
            self.get_serializer():获取序列化器
            self.get_object():获取指定的单一对象 注意：查询参数的变量名必须为pk
"""


# DRF的视图函数
class UserList(GenericAPIView):
    # 查询集对象
    queryset = UserInfo.objects.all()
    # 序列化器
    serializer_class = UserInfoSerializer01

    def get(self, request, format=None):
        # 获取方法
        data = self.get_queryset()
        us = self.get_serializer(data, many=True)
        result = {"code": 200, "message": "success", "data": us.data}
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        prams = request.data
        us = self.get_serializer(data=prams)
        if us.is_valid():
            us.save()
            return Response({"code": 201, "message": "success", "data": us.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"code": 402, "message": us.errors}, status=status.HTTP_402_PAYMENT_REQUIRED)


class UserDetaill(GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01

    def get(self, request, pk):
        obj = self.get_object()
        data = self.get_serializer(obj)
        return Response({"code": 200, "message": "success", "data": data.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        prams = request.data
        # 通过序列化更新数据
        us = self.get_serializer(self.get_object(), data=prams)
        if us.is_valid():
            us.save()
            return Response({"code": 202, "message": "success", "data": us.initial_data},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": 403, "message": us.errors}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response({"code": 203, "message": "success"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
