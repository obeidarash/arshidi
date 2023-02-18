from django.shortcuts import redirect, render
from financial.models import Expense
from django.db.models import Sum

def home(request):
    expenses = Expense.objects.aggregate(Sum('price'))
    print(type(expenses))

    context = {
        'expenses_sum': expenses['price__sum']
    }
    return render(request, 'index.html', context)
