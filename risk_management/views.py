from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RiskForm, DepartmentForm, EmployeeForm
from .models import Risk, Department, Employee



# Create your views here.

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
     
     
     return render(request, 'risk_management/home.html', context)


def create_risk(request):
     form =RiskForm()

     if request.method == 'POST':
          form = RiskForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/form.html', context )



def update_risk(request, pk):
     
     risk = Risk.objects.get(id=pk)
     form =RiskForm(instance=risk)

     if request.method == 'POST':
          form = RiskForm(request.POST, instance=risk )
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/form.html', context )



def delete_risk(request, pk):
     risk = Risk.objects.get(id=pk)

     if request.method == 'POST':
               risk.delete()
               return redirect('home')


     return render(request,'risk_management/delete.html',{'obj':risk} )


def view_risk(request, pk):
     
     risk = Risk.objects.get(id=pk)
     return render(request,'risk_management/view.html',{'obj':risk,'id':"im risk"} )





def create_department(request):
     form =DepartmentForm()

     if request.method == 'POST':
          form = DepartmentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/form.html', context )




def delete_department(request, pk):
     department = Department.objects.get(id=pk)

     if request.method == 'POST':
               department.delete()
               return redirect('home')


     return render(request,'risk_management/delete.html',{'obj':department} )





def create_employee(request):
     form =EmployeeForm()

     if request.method == 'POST':
          form = EmployeeForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/form.html', context )



def update_employee(request, pk):
     
     employee = Employee.objects.get(id=pk)
     form = EmployeeForm(instance=employee)

     if request.method == 'POST':
          form = EmployeeForm(request.POST, instance=employee )
          if form.is_valid():
               form.save()
               return redirect('home')


     context = {'form':form}
     return render(request,'risk_management/form.html', context )





def delete_employee(request, pk):
     employee = Employee.objects.get(id=pk)

     if request.method == 'POST':
               employee.delete()
               return redirect('home')


     return render(request,'risk_management/delete.html',{'obj':employee} )



def view_employee(request, pk):
     
     employee = Employee.objects.get(id=pk)
    
     return render(request,'risk_management/view.html',{'obj':employee, 'id':"im employee"} )

