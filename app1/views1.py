from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

"""
@api_view()定义视图函数
"""


# Create your views here.
@api_view(['GET', 'POST'])
def user_list1(request, format=None):
    # get请求查询用户列表
    if request.method == "GET":
        data = UserInfo.objects.all()
        us = UserInfoSerializer01(data, many=True)
        result = {"code": 200, "message": "success", "data": us.data}
        return Response(result, status=status.HTTP_200_OK)
    # post请求添加用户信息
    elif request.method == "POST":
        # request对象不是dgango的原生request对象request.data用来接受请求的数据request.query_params接收url后面的参数
        prams = request.data
        us = UserInfoSerializer01(data=prams)
        if us.is_valid():
            us.save()
            return Response({"code": 201, "message": "success", "data": us.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"code": 402, "message": us.errors}, status=status.HTTP_402_PAYMENT_REQUIRED)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail1(request, id):
    # 获取单个用户，修改用户信息，删除用户信息
    try:
        obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return Response({"code": 403, "message": "数据不存在"}, status=status.HTTP_403_FORBIDDEN)
    if request.method == "GET":
        data = UserInfoSerializer01(obj)
        return Response({"code": 200, "message": "success", "data": data.data}, status=status.HTTP_200_OK)
    if request.method == "PUT":
        prams = request.data
        # 通过序列化更新数据
        us = UserInfoSerializer01(obj, data=prams)
        if us.is_valid():
            us.save()
            return Response({"code": 202, "message": "success", "data": us.initial_data},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": 403, "message": us.errors}, status=status.HTTP_403_FORBIDDEN)
    elif request.method == "DELETE":
        obj.delete()
        return Response({"code": 203, "message": "success"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
