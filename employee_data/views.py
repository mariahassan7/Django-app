from django.shortcuts import render
from employee_data.models import Employee

def employee_data(request):
    return render(request, "employee_data.html",{})
# Create your views here.

def homepage(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, 'homepage.html', context)

def employee(request, id):
    employee =Employee.objects.get(id=id)
    context = {
        'employee': employee
    }
    return render(request, 'employee.html',context)
