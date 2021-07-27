from django.shortcuts import render, redirect
from Register.forms import EmployeeForm
from Register.models import Employee


def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "register/employee_form.html", {"form": form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "register/employee_list.html", context)

