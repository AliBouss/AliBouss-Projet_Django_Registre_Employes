from django.contrib import admin

from Register.models import Employee


class AdminEmployee(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'emp_code', 'phone' ]


admin.site.register(Employee, AdminEmployee)
