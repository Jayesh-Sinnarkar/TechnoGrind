from django.contrib import admin
from .models.Employee import Employee
# Register your models here.

admin.site.register(Employee)

class  EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name')

