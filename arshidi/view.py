from django.shortcuts import redirect, render
from financial.models import Expense, Income, Salary
from django.db.models import Sum

def home(request):
    expenses = Expense.objects.aggregate(Sum('price'))
    incomes = Income.objects.aggregate(Sum('price'))
    salaries = Salary.objects.aggregate(Sum('price'))

    # net income based on US Dollar = 500,000 Rial
    dollar = 500000
    salaries['price__sum'] = salaries['price__sum'] or 0
    incomes['price__sum'] = incomes['price__sum'] or 0
    expenses['price__sum'] = expenses['price__sum'] or 0

    net_income = (incomes['price__sum'] * dollar) - (expenses['price__sum'] + salaries['price__sum'])

    context = {
        'expenses_sum': expenses['price__sum'],
        'incomes_sum': incomes['price__sum'],
        'salaries_sum': salaries['price__sum'],
        'net_income': net_income,
    }
    return render(request, 'index.html', context)
