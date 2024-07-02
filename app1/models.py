from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    pwd = models.CharField(max_length=18, verbose_name="密码")
    email = models.EmailField(max_length=30, verbose_name='邮箱')
    age = models.IntegerField(verbose_name='年龄', default=18)

    class Meta:
        db_table = 'user'
        verbose_name = "用户表"

    def __str__(self):
        return self.name


class Addr(models.Model):
    user = models.ForeignKey('UserInfo', verbose_name='所属用户', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="手机号", max_length=18)
    city = models.CharField(verbose_name="城市", max_length=10)
    info = models.CharField(verbose_name='地址详情', max_length=200)

    class Meta:
        db_table = 'addr'
        verbose_name = '邮件地址表'

    def __str__(self):
        return self.user


class ResultBody(models.Model):
    psp = models.CharField(verbose_name="机构名", max_length=300)
    mid = models.CharField(verbose_name='商户id', max_length=300)
    data = models.TextField(verbose_name='文本数据')
    time = models.DateTimeField(verbose_name="获取时间")

    class Meta:
        db_table = 'result'
        verbose_name = "存储接受到的响应数据"

    def __str__(self):
        return self.data


# 文件模型类需要下载相关依赖 pip install Pillow
class Files(models.Model):
    file_name = models.ImageField()

    class Meta:
        db_table = 'files'
        verbose_name = '文件存储'

    def __str__(self):
        return self.path
