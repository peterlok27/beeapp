from django import forms
from django.forms import widgets
from .models import *

class Expense_Form(forms.ModelForm):
    class Meta: 
        model = Expense
        fields = ['Expense' ,'Category']
        widgets = {
            'Expense'   : widgets.NumberInput(),
            'Category'  : widgets.Select() 
        }

class Budget_Form(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['Total_Budget' , 'Savings_Percentage']
