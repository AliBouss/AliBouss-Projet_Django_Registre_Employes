from django.shortcuts import render
from Register.forms import EmployeeForm


def employee_form(request):
    form = EmployeeForm()
    return render(request, "register/employee_form.html", {"form": form})


def employee_list(request):
    return render(request, "register/employee_list.html")

