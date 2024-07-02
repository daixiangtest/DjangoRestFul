"""
URL configuration for djangoRestFul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from app1.views1 import *
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views2, views3, views4, views5, views6, views7, views8, views9
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from app1.views9 import TokenLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加drf自带的接口文档
    path("docs/", include_docs_urls(title='接口文档')),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login1/', TokenLogin.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("list/", user_list),
    path('detail/<int:id>/', user_detail),
    path("list1/", user_list1),
    path('detail1/<int:id>/', user_detail1),
    path("list2/", views5.UserList.as_view()),
    path('detail2/<int:pk>/', views5.UserDetaill.as_view()),
    path("list3/", views6.UserList.as_view({'get': 'list', 'post': 'create'})),  # 指定的为minx类中的方法名
    path('detail3/<int:pk>/', views6.UserList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('webhook/<str:psp>/<int:mid>/', views7.WebHook.as_view()),
    # path('files/', views9.UpFile.as_view({'get': 'list', 'post': 'create'}))
    path('image/<str:name>', views9.upload)
]

router = routers.SimpleRouter()  # 创建router对象并注册
router.register("view", views8.UserList)  # 输入（路径,视图类）自己生成url的匹配路径
router.register('files', views9.UpFile)

print(
    router.urls)  # [<URLPattern '^view/$' [name='userinfo-list']>, <URLPattern '^view/(?P<pk>[^/.]+)/$' [name='userinfo-detail']>]
urlpatterns += router.urls
# 修饰url的后缀，可以通过.json与.api展示不同的结果通过format参数来展示效果
urlpatterns = format_suffix_patterns(urlpatterns)
