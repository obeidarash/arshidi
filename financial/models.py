from django.db import models
from tinymce.models import HTMLField
from management.models import Project
from human_resources.models import Employee
import os
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

CURRENCY = [
    ('IRR', 'Rial'),
    ('USD', 'US Dollar'),
    ('USDT', 'Tether'),
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


class Expense(models.Model):
    title = models.CharField(max_length=512, help_text='Buy VPS')
    to = models.CharField(max_length=256, help_text="UpWork, Uber ETC")
    price = models.BigIntegerField()
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    date = models.DateField(verbose_name='Pay Date')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    link = models.URLField(null=True, blank=True)
    attach = models.FileField(blank=True, null=True, upload_to=upload_file_path)
    comment = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Salary(models.Model):
    title = models.CharField(max_length=512, help_text='2nd payment to mr X')
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    price = models.BigIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Pay Date')
    attach = models.FileField(blank=True, null=True, upload_to=upload_file_path)
    comment = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: you can connected to timesheet and automatically calculate hours or price with signals

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Salaries'


class Income(models.Model):
    title = models.CharField(max_length=512, help_text='2nd payment from Django project X')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[1], max_length=64)
    price = models.BigIntegerField()
    date = models.DateField(verbose_name='Income Date')
    link = models.URLField(null=True, blank=True)
    attach = models.FileField(blank=True, null=True, upload_to=upload_file_path)
    comment = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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
