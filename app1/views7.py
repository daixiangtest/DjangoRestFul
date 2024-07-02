import datetime

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404

"""
webhook接受函数
"""


# DRF的视图函数
class WebHook(APIView):
    # 指定认证方式
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)
    def get(self, request, psp, mid):
        data = ResultBody.objects.filter(psp=psp, mid=mid)
        us = ResultBodySerializer(data, many=True)
        result = {"code": 200, "message": "success", "data": us.data}
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, psp, mid):
        print(request.body.decode())
        try:
            prams = request.data
        except Exception as e:
            prams = request.body.decode()
        date = datetime.datetime.now()
        data = {'psp': psp, 'mid': mid, 'data': str(prams), 'time': date}
        us = ResultBodySerializer(data=data)
        if us.is_valid():
            us.save()
            return Response({"code": 201, "message": "success", "data": us.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"code": 402, "message": us.errors}, status=status.HTTP_402_PAYMENT_REQUIRED)
