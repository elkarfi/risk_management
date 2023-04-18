from django.contrib import admin
from risk_management.models import Department, Employee, Risk

# Register your models here.

admin.site.register(Risk)
admin.site.register(Department)
admin.site.register(Employee)


