from django.contrib import admin
from restapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'email' )
    ordering = ('-id',)
    search_fields = ('id',)
    # readonly_fields = ("created", "updated",)
    list_per_page = 50

admin.site.register(Student, StudentAdmin)