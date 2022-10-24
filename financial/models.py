from django.db import models
from tinymce.models import HTMLField
from management.models import Project

CURRENCY = [
    ('IRR', 'Rial'),
    ('USD', 'US Dollar'),
]


class Expense(models.Model):
    title = models.CharField(max_length=512, help_text='Buy VPS')
    price = models.BigIntegerField()
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    date = models.DateField(verbose_name='Pay Date')
    link = models.URLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: add attach file, to (contacts), project

    def __str__(self):
        return self.title


class Salary(models.Model):
    title = models.CharField(max_length=512, help_text='2nd payment to mr X')
    price = models.BigIntegerField()
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    date = models.DateField(verbose_name='Pay Date')
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: add attach, to

    class Meta:
        verbose_name_plural = 'Salaries'


class Income(models.Model):
    title = models.CharField(max_length=512, help_text='2nd payment from Django project X')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[1], max_length=64)
    date = models.DateField(verbose_name='Income Date')
    link = models.URLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: Project
