"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Register.views import EmployeeList, EmployeeCreate, EmployeeDetail, HomeView, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('create/', EmployeeCreate.as_view(), name="form"),  # insert data
    path('list/', EmployeeList.as_view(), name="list"),  # display records
    path('detail/<int:pk>/', EmployeeDetail.as_view(), name="detail"),
    path('update/<int:pk>/', EmployeeUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', EmployeeDelete.as_view(), name="delete"),

]

