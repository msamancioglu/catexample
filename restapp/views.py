# from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerialiser
from .pagination import AppPagination


class StudentList(ListAPIView, CreateModelMixin):
    serializer_class = StudentSerialiser
    # filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = {
        'id': ['exact'],
        # 'otel': ['exact'],

    }
    search_fields = ('id',)
    ordering_fields = '__all__'
    ordering = ['created']
    #    permission_classes = [IsAuthenticated]
    pagination_class = AppPagination

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = StudentSerialiser(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            responseData = {
                'status': status.HTTP_201_CREATED,
                'message': 'Student objects created'
            }
        else:
            responseData = {
                'errors': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Student objects can not created'
            }
        return JsonResponse(responseData)


class StudentChange(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser
    #    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        self.serializer_class = StudentSerialiser
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(updatedby=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.isActive:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            responseData = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Object Not Found'
            }
            return JsonResponse(responseData)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        responseData = {
            'status': status.HTTP_204_NO_CONTENT,
            'message': 'Student object has been deleted'

        }
        return JsonResponse(responseData)

    def perform_destroy(self, instance):
        # instance.isActive = False
        # instance.updatedby = self.request.user
        instance.save()