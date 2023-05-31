from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RiskForm, DepartmentForm, EmployeeForm
from .models import Risk, Department, Employee
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.



@login_required(login_url="welcome")
def home(request):
     risks = Risk.objects.all()
     total_risk = Risk.objects.count()
     opened = Risk.objects.filter(status="opened").count()
     closed = Risk.objects.filter(status="closed").count()


     departments = Department.objects.all()
     employees = Employee.objects.all()

     context = {
           
          "risks":risks,
          "departments":departments,
          "employees":employees,
          "total_risk":total_risk,
          "opened":opened,
          "closed":closed



               }
     
     
     return render(request, 'risk_management/new_home.html', context)




@login_required(login_url="welcome")
def create_risk(request):
     form =RiskForm()

     if request.method == 'POST':
          form = RiskForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/new_risk_form.html', context )



@login_required(login_url="welcome")
def update_risk(request, pk):
     
     risk = Risk.objects.get(id=pk)
     form =RiskForm(instance=risk)

     if request.method == 'POST':
          form = RiskForm(request.POST, instance=risk )
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/new_risk_form.html', context )



@login_required(login_url="welcome")
def delete_risk(request, pk):
     risk = Risk.objects.get(id=pk)

     if request.method == 'POST':
               risk.delete()
               return redirect('home')


     return render(request,'risk_management/new_delete.html',{'obj':risk} )




@login_required(login_url="welcome")
def create_department(request):
     form =DepartmentForm()

     if request.method == 'POST':
          form = DepartmentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/new_department_form.html', context )




@login_required(login_url="welcome")
def delete_department(request, pk):
     department = Department.objects.get(id=pk)

     if request.method == 'POST':
               department.delete()
               return redirect('home')


     return render(request,'risk_management/new_delete.html',{'obj':department} )




@login_required(login_url="welcome")
def view_department(request):
     
     department = Department.objects.all()
    
     return render(request,'risk_management/employee_table.html',{'obj':department, 'id':"im department"} )








@login_required(login_url="welcome")
def create_employee(request):
     form =EmployeeForm()

     if request.method == 'POST':
          form = EmployeeForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/new_employee_form.html', context )


@login_required(login_url="welcome")
def update_employee(request, pk):
     
     employee = Employee.objects.get(id=pk)
     form = EmployeeForm(instance=employee)


     if request.method == 'POST':
          form = EmployeeForm(request.POST, instance=employee )
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/edit_employee.html', context )




@login_required(login_url="welcome")
def delete_employee(request, pk):
     employee = Employee.objects.get(id=pk)

     if request.method == 'POST':
               employee.delete()
               return redirect('home')


     return render(request,'risk_management/new_delete.html',{'obj':employee} )



@login_required(login_url="welcome")
def view_employee(request):
     
     employee = Employee.objects.all()

     return render(request,'risk_management/employee_table.html',{'obj':employee,'id':"im employee"} )





def login_page(request):

     if request.user.is_authenticated:
           return redirect('home')



     if request.method == 'POST':
           username= request.POST.get('username')
           password= request.POST.get('password')

           try:

               user = User.objects.get(username=username)

           except:

               messages.error(request, 'User does not exist')


           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)
               messages.success(request, "You have successfully Logged In.")
               return redirect('home')
           else:
               messages.error(request, 'Username OR password does not exit')

     context = {}
     return render(request,'risk_management/new_login.html',context )

   

def logout_employee(request):
          logout(request)
          return redirect('login')