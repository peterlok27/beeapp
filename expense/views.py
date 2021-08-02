from django.shortcuts import render
from .forms import *
# Create your views here.
def home_view(request): 

    return render(request , 'base.html' , {}) 

def expense(request):
    context = {}
    form = Expense_Form()
    if request.method == "POST" :
        form = Expense_Form(request.POST)
        if form.is_valid():
            form.save() 
            print("expense")
    context['form'] = form

    budget = Budget_Form()
    if request.method == "POST" : 
        budget = Budget_Form(request.POST) 
        if budget.is_valid():
            budget.save() 
            print("BUDGET")
    context['budget'] = budget 

    return render(request , "expense.html" , context) 