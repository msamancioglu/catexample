from rest_framework.pagination import PageNumberPagination


class AppPagination(PageNumberPagination):
    page_size = 100

