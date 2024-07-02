from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from .models import *
from .serializers import *


# Create your views here.

def user_list(request):
    # get请求查询用户列表
    if request.method == "GET":
        data = UserInfo.objects.all()
        us = UserInfoSerializer01(data, many=True)
        return JsonResponse({"code": 200, "message": "success", "data": us.data})
    # post请求添加用户信息
    elif request.method == "POST":
        # prames = JSONParser().parse(request)
        prames = request.POST if len(request.POST) > 0 else JSONParser().parse(request)
        us = UserInfoSerializer01(data=prames)
        if us.is_valid():
            us.save()
            return JsonResponse({"code": 201, "message": "success", "data": us.data})
        else:
            return JsonResponse({"code": 402, "message": us.errors})
    else:
        return JsonResponse({"code": 401, "message": "不支持该请求"})


def user_detail(request, id):
    # 获取单个用户，修改用户信息，删除用户信息
    try:
        obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return JsonResponse({"code": 403, "message": "数据不存在"})
    if request.method == "GET":
        data = UserInfoSerializer01(obj)
        return JsonResponse({"code": 200, "message": "success", "data": data.data})
    if request.method == "PUT":
        parmes = request.POST if len(request.POST) > 0 else JSONParser().parse(request)
        # 通过序列化更新数据
        us = UserInfoSerializer01(obj, data=parmes)
        if us.is_valid():
            us.save()
            return JsonResponse({"code": 202, "message": "success", "data": us.initial_data})
        else:
            return JsonResponse({"code": 403, "message": us.errors})
    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({"code": 203, "message": "success"})


