from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView, DeleteView
from Register.models import Employee


class HomeView(TemplateView):
    title = 'default'
    template_name = 'register/home.html'


class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = "register/employee_list.html"


class EmployeeDetail(DetailView):
    model = Employee
    context_object_name = 'detail'
    template_name = "register/employee_detail.html"


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('list')
    template_name = "register/employee_form.html"


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('list')
    template_name = "register/employee_form.html"


class EmployeeDelete(DeleteView):
    model = Employee
    context_object_name = 'delete'
    success_url = reverse_lazy('list')
    template_name = "register/delete_confirm.html"




"""
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html", {"form": form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_list(request):
    context = {'employee_list.html': Employee.objects.all()}
    return render(request, "register/employee_list.html", context)
    
def employee_delete(request)
"""