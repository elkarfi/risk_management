from django.forms import ModelForm
from django import forms
from .models import Risk, Department, Employee

class RiskForm(ModelForm):
        class Meta:
            model  =   Risk
            fields = '__all__'


class DepartmentForm(ModelForm):
        class Meta:
            model  =   Department
            fields = '__all__'


class EmployeeForm(ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)
        class Meta:
            model  =   Employee
            fields = '__all__'

