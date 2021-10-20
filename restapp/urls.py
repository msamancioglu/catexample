from django.urls import path
from .views import *

urlpatterns = [
        path('students', StudentList.as_view(), name='Stident Create List'),
        path('student/<int:id>', StudentChange.as_view(), name='Read Delete Update'),
    ]