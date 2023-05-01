from django import forms
from django.db import models
from tinymce.models import HTMLField
# from management.models import Project
import management.models
from human_resources.models import Employee
import os
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save, post_save
from contacts.models import Company
SOURCE = [
    ('employee', 'Employee'),
    ('company', 'Company')
]

CURRENCY = [
    ('USD', 'US Dollar'),
    ('USDT', 'Tether'),
    ('IRR', 'Rial'),
]


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_file_path(instance, filename):
    from time import time
    uid = str(uuid.uuid4().hex)[:10]
    name, ext = get_filename_ext(filename)
    time = str(time())
    final_name = f"{uid}{time[:10:-1]}{ext}"
    return f"financial/{final_name}"


class Currency(models.Model):
    title = models.CharField(max_length=128, help_text="Rial or US Dollar", unique=True)
    code = models.SlugField(unique=True)
    crypto = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title + f" ({self.code})"

    class Meta:
        verbose_name_plural = 'Currencies'


# class Wallet(models.Model):
#     title = models.CharField(max_length=128, help_text="name of the wallet", unique=True)
#     currency = models.ForeignKey(Currency, null=False, blank=False, on_delete=models.CASCADE)
#     network = models.CharField(max_length=64, null=False, blank=False)
#     address = models.CharField(max_length=256, null=False, blank=False)
#     created = models.DateTimeField(auto_now_add=True, null=True)
#     updated = models.DateTimeField(auto_now=True, null=True)
#
#     def __str__(self):
#         return self.currency.title + f" ({self.currency.code})" + " - " + self.network

class Category(models.Model):
    title = models.CharField(max_length=128, help_text="Office Supplies or Memberships fees", unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Bank(models.Model):
    name = models.CharField(max_length=128, help_text="Resalat or Meli", unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=False, null=True, help_text="Bank name")
    card_number = models.CharField(max_length=20, null=True, blank=True,
                                   help_text="16 Digits card number without dash")
    account_number = models.CharField(max_length=40, null=True, blank=True, help_text="Shomare Hesab")
    sheba = models.CharField(max_length=80, null=True, blank=True, help_text='Without IR')
    phone_number = models.CharField(max_length=40, null=True, blank=True, help_text="example: +989981105577")
    email = models.EmailField(max_length=40, null=True, blank=True, help_text="Mostly for paypal account")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.firstname + " " + self.owner.lastname + " - " + str(self.bank)


class Expense(models.Model):
    title = models.CharField(max_length=512, help_text='Buy VPS', null=True)
    to = models.ForeignKey(Company, on_delete=models.CASCADE, help_text="UpWork, Uber ETC", null=True, blank=False)
    price = models.BigIntegerField(null=True, help_text="Be careful with zeros!")
    currency = models.ForeignKey(Currency, null=False, blank=False, on_delete=models.CASCADE)
    source = models.CharField(choices=SOURCE, default=SOURCE[0], max_length=32, help_text="Who payed this expense?")
    payer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, help_text="https://www.brex.com/journal/business-expense-categories")
    date = models.DateField(verbose_name='Pay Date', null=True)
    project = models.ForeignKey('management.Project', related_name='expense_project', on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    link = models.URLField(null=True, blank=True)
    attach = models.FileField(blank=True, null=True, upload_to=upload_file_path)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Salary(models.Model):
    advance_payment = models.BooleanField(default=False, help_text="Prepayment or advance payment to the freelancer")
    currency = models.ForeignKey(Currency, null=False, blank=False, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, verbose_name="To employee")
    date = models.DateField(verbose_name='Pay Date', null=True)
    project = models.ManyToManyField('management.Project', related_name='salary_project', blank=True,
                                     verbose_name="Project(s)")
    bank_account = models.ForeignKey(BankAccount, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name="To bank account")
    attach = models.FileField(blank=True, null=True, upload_to=upload_file_path)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.employee.firstname) + " " + str(self.employee.lastname) + ": " + str(
            self.price) + " " + str(self.currency)

    class Meta:
        verbose_name_plural = 'Salaries'


class Income(models.Model):
    # title = models.CharField(max_length=512, help_text='2nd payment from Django project X', null=True, blank=True)
    project = models.ForeignKey('management.Project', related_name='income_project', on_delete=models.CASCADE,
                                null=True)
    date = models.DateField(verbose_name='Income Date', null=True)
    price = models.FloatField(null=True)
    currency = models.ForeignKey(Currency, null=True, blank=False, on_delete=models.CASCADE)
    # wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Wallet Address')
    bank = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Bank Account')
    link = models.URLField(null=True, blank=True)
    attach = models.FileField(blank=True, null=True, upload_to=upload_file_path)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.project.title


# delete attach file after model has been deleted
@receiver(post_delete, sender=Expense)
def post_save_expense(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.attach.delete(save=False)
    except:
        pass


# update attach file after model has been updated
@receiver(pre_save, sender=Expense)
def pre_save_expense(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).attach.path
        try:
            new_img = instance.attach.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass


@receiver(post_delete, sender=Salary)
def post_save_salary(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.attach.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Salary)
def pre_save_salary(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).attach.path
        try:
            new_img = instance.attach.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass


@receiver(post_delete, sender=Income)
def post_save_income(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.attach.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Income)
def pre_save_income(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).attach.path
        try:
            new_img = instance.attach.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
