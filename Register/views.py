from django.shortcuts import render, redirect
from Register.forms import EmployeeForm
from Register.models import Employee


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html", {"form": form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('list/')


def employee_list(request):
    context = {"employee_list": Employee.objects.all()}
    return render(request, "register/employee_list.html", context)

