from .serializers import *
from rest_framework import generics

"""
视图扩展类：1、CreateAPIView
        继承自： GenericAPIView、CreateModelMixin
        提供 post 方法
        2、ListAPIView
        继承自：GenericAPIView、ListModelMixin
        提供 get 方法
        3、RetireveAPIView
        继承自: GenericAPIView、RetrieveModelMixin
        提供 get 方法
        4、DestoryAPIView
        继承自：GenericAPIView、DestoryModelMixin
        提供 delete 方法
        5、UpdateAPIView
        继承自：GenericAPIView、UpdateModelMixin
        提供 put 和 patch 方法
        6、RetrieveUpdateAPIView
        继承自： GenericAPIView、RetrieveModelMixin、UpdateModelMixin
        提供 get、put、patch方法
        7、RetrieveUpdateDestoryAPIView
        继承自：GenericAPIView、RetrieveModelMixin、UpdateModelMixin、
        DestoryModelMixin
        提供 get、put、patch、delete方法

"""


# DRF的视图函数
class UserList(generics.ListAPIView, generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01


class UserDetaill(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer01
