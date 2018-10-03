from rest_framework.pagination import CursorPagination


class CursorOrderByIdPagination(CursorPagination):
    ordering = '-id'
    page_size_query_param = 'page_size'
