from django.db import models

# Create your models here.



class Department(models.Model):
        name_department= models.CharField(max_length=255)

        def __str__(self):
                return self.name_department


class Employee(models.Model):
        first_name= models.CharField(max_length=255)
        last_name= models.CharField(max_length=255)
        department= models.ForeignKey(Department,on_delete=models.CASCADE)
        username = models.CharField(max_length = 10, unique = True, db_index = True)
        password = models.CharField(max_length=100)

        def __str__(self):
                return self.first_name
        


class Risk(models.Model):
        risk_description= models.TextField()
        severity= models.IntegerField()
        status= models.CharField(max_length=255)
        action_taken= models.TextField()
        end_date= models.DateField()
        department= models.ForeignKey(Department,on_delete=models.CASCADE)
        employee= models.ForeignKey(Employee,on_delete=models.CASCADE)
        last_update= models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.risk_description

