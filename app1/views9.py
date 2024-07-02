import rest_framework_simplejwt
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from djangoRestFul.settings import MEDIA_URL
from .serializers import *
from rest_framework import generics, mixins

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
class UpFile(mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.ListModelMixin,
             GenericViewSet):
    serializer_class = FilesSerializer
    queryset = Files.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        pic = request.data['file_name']
        print(pic)
        size = pic.size
        name = pic.name
        type = pic.content_type
        # 可以判断文件大小
        print(size)
        # 可以判断文件名称是否重复
        print(name)
        # 可以判断文件类型
        print(type)
        if size > 1024 * 300:
            return Response({'msg': '文件过大'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # 获取文件对象那
        pic = self.get_object()
        path = pic.file_name.path
        return FileResponse(open(path, 'rb'))


def upload(request, name):
    path = "files/" + MEDIA_URL + name
    return FileResponse(open(path, 'rb'))


# token鉴权需要安装依赖库来实现  pip install djangorestframework-simplejwt
# 自定义登录视图
class TokenLogin(TokenObtainPairView):
    # 重写继承类的登录方法
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # 通过serializer中的属性值来定义返回的内容
        result = serializer.validated_data
        result['token'] = result.pop('access')
        result['user'] = serializer.user.username
        return Response(result, status=status.HTTP_200_OK)
