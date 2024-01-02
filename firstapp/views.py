from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Employee
# Create your views here.
def firstapp(request):
    if request.method =="post":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        salary=request.POST['salary']
        age=request.POST['age']
        gender=request.POST['gender']
        email=request.POST['email']
        domain =request.POST['domain']
        company =request.POST['company']
        experience=request.POST['experience']
        employee =Employee(firstname =firstname,lastname =lastname,salary =salary,age =age,gender =gender,email =email,domain=domain,company=company,experience =experience)
        employee.save()

    return render(request, "index.html")
def data(request):
    emp =Employee.objects.all()
    return render(request, "data.html",{"Employees" : emp})