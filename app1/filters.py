from django_filters import rest_framework as filters
from app1.models import UserInfo

"""
自定义的过滤器
"""


class UserInfoFilter(filters.FilterSet):
    # 定义过滤字段的筛选规范
    min = filters.NumberFilter(field_name='age', lookup_expr='gte')
    max = filters.NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = UserInfo
        # 模型类中的需要过滤的字段
        fields = ['age']
