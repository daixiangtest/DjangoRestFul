from rest_framework.pagination import PageNumberPagination

"""
自定义的分页管理类
"""


# 在视图函数中pagination_class = 类名来指定自定义类的过滤 关闭分页功能只需在视图函数中设置pagination_class = None
class StuPagination(PageNumberPagination):
    # 默认每页数据量
    page_size = 20
    # 指定页面的查询参数名称
    page_size_query_param = 'page_size'
    # 每页的数据量的最大值
    max_page_size = 10000
