from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404

"""
@api_view()定义视图函数
"""


# DRF的视图函数
class UserList(APIView):
    def get(self, request, format=None):
        data = UserInfo.objects.all()
        us = UserInfoSerializer01(data, many=True)
        result = {"code": 200, "message": "success", "data": us.data}
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        prams = request.data
        us = UserInfoSerializer01(data=prams)
        if us.is_valid():
            us.save()
            return Response({"code": 201, "message": "success", "data": us.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"code": 402, "message": us.errors}, status=status.HTTP_402_PAYMENT_REQUIRED)


class UserDetaill(APIView):
    def get_object(self, id):
        try:
            return UserInfo.objects.get(id=id)
        except Exception as e:
            raise Http404

    def get(self, request, id):
        data = UserInfoSerializer01(self.get_object(id))
        return Response({"code": 200, "message": "success", "data": data.data}, status=status.HTTP_200_OK)

    def put(self, request, id):
        prams = request.data
        # 通过序列化更新数据
        us = UserInfoSerializer01(self.get_object(id), data=prams)
        if us.is_valid():
            us.save()
            return Response({"code": 202, "message": "success", "data": us.initial_data},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": 403, "message": us.errors}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, id):
        self.get_object(id).delete()
        return Response({"code": 203, "message": "success"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
