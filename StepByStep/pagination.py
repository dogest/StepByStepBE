from rest_framework.pagination import CursorPagination


# 修改原有的翻页，使其基于 id 排序，同时添加 page_size 用于前端控制返回条数
class CursorOrderByIdPagination(CursorPagination):
    ordering = '-id'
    page_size_query_param = 'page_size'
