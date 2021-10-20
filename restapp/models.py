from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name="Students name", max_length=100)
    lastname = models.CharField(verbose_name="Students Last name", max_length=100)
    email = models.CharField(verbose_name="Students email", max_length=100)


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name