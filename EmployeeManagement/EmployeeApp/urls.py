
from django.contrib import admin
from django.urls import path, include
import EmployeeApp.views as EmployeeView


urlpatterns = [
    path('', EmployeeView.Overview, name='employee-overview'),
]
