from django.db import models
import time as tm
import datetime
# Create your models here.
class Budget(models.Model): 
    Total_Budget = models.IntegerField() 
    Savings_Percentage = models.IntegerField() 

class Expense(models.Model): 
    CHOICES = [
        ('Food' , 'Food'),
        ('Shopping' , 'Shopping'),
        ('Transportation' , 'Transportation'),
        ('Bills' , 'Bills')
    ]
    Expense = models.FloatField() 
    Category = models.CharField(choices=CHOICES , max_length=1000) 
    DateTime = models.DateTimeField(auto_now_add=True)