from rest_framework import serializers
from .models import *

"""
序列化器的作用：对数据进行校验 对数据对象进行转换
    进行序列化操作，将ORM对象 转换为json数
    进行反序列化，将json数据转换为ORM对象
"""


# 序列化器的定义类属性字段名需要与对应的模型类字段属性一致
class UserInfoSerializer(serializers.Serializer):
    # 序列化主要用来处理模型里面的对应字段所有属性名需要与模型类的属性名一致才可以
    name = serializers.CharField(help_text="用户信息", max_length=20, required=True)
    pwd = serializers.CharField(help_text="密码", min_length=6, required=True)
    email = serializers.EmailField(help_text="邮箱", required=True)
    age = serializers.IntegerField(help_text="年龄", required=True, max_value=100, min_value=0)

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.pwd = validated_data['pwd']
        instance.email = validated_data['email']
        instance.age = validated_data['age']
        instance.save()


class AddrSerializer(serializers.Serializer):
    # 关联字段系列化
    user = serializers.StringRelatedField
    phone = serializers.CharField(help_text='手机号', max_length=18)
    city = serializers.CharField(help_text='城市', max_length=10)
    info = serializers.CharField(help_text='详细地址', max_length=200)

    def create(self, validated_data):
        Addr.objects.create(**validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.user = validated_data['user']
        instance.phone = validated_data['phone']
        instance.city = validated_data['city']
        instance.info = validated_data['info']
        instance.save()


# 通过序列化吗模型来创建序列化
class UserInfoSerializer01(serializers.ModelSerializer):
    class Meta:
        # 选择序列化的模型对象
        model = UserInfo
        # 选择参与序列化的字段
        fields = "__all__"

    # 对字段进行自定义的校验规则 写法validate_字段名（value）:
    # def validate_pwd(value):
    #     if not (6 < len(value) < 10):
    #         raise serializers.ValidationError


class AddrSerializer01(serializers.ModelSerializer):
    class Meta:
        model = Addr
        # 排除不需要参与序列化的字段
        exclude = ('id',)


class ResultBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultBody
        fields = "__all__"


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"


