from django.db import models

# Create your models here.

class Position(models.Model) : 
    employee_title = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.employee_title

class Employee(models.Model) : 
    full_name = models.CharField(max_length=100)
    employee_no = models.CharField(max_length=3)
    mobile_no = models.CharField(max_length=10)
    employee_position = models.ForeignKey(Position, on_delete=models.CASCADE)

