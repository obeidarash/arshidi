from django.db import models
from tinymce.models import HTMLField
from management.models import Project
from human_resources.models import Employee
CURRENCY = [
    ('IRR', 'Rial'),
    ('USD', 'US Dollar'),
    ('USDT', 'Tether'),
]


class Expense(models.Model):
    title = models.CharField(max_length=512, help_text='Buy VPS')
    to = models.CharField(max_length=256, help_text="UpWork, Uber ETC")
    price = models.BigIntegerField()
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    date = models.DateField(verbose_name='Pay Date')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    link = models.URLField(null=True, blank=True)
    comment = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: add attach file

    def __str__(self):
        return self.title


class Salary(models.Model):
    title = models.CharField(max_length=512, help_text='2nd payment to mr X')
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    price = models.BigIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Pay Date')
    comment = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: add attach, you can connected to timesheet

    class Meta:
        verbose_name_plural = 'Salaries'


class Income(models.Model):
    title = models.CharField(max_length=512, help_text='2nd payment from Django project X')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[1], max_length=64)
    price = models.BigIntegerField()
    date = models.DateField(verbose_name='Income Date')
    link = models.URLField(null=True, blank=True)
    comment = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: Attach
