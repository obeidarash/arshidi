from django.db import models
from tinymce.models import HTMLField
from django_countries.fields import CountryField
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
import os
import uuid


GENDER = [
    ('Mr', 'Mr'),
    ('Ms', 'Ms')
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
    return f"human_resources/{final_name}"


class Position(models.Model):
    title = models.CharField(max_length=128, help_text="Web Developer or Front End Developer", unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=128, help_text="Git or Django", unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Employee(models.Model):  # Todo: Think more about the name
    gender = models.CharField(choices=GENDER, max_length=64)
    is_active = models.BooleanField(default=True, blank=False, null=False, help_text='This person is currently working')
    firstname = models.CharField(max_length=128, null=True)
    lastname = models.CharField(max_length=128)
    # Contact
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, help_text="With dial code: +989125558877", max_length=64)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    birthday = models.DateField()
    skills = models.ManyToManyField(Skill)
    positions = models.ManyToManyField(Position)
    # Address
    country = CountryField(null=True, blank=True, blank_label='select country')
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)

    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    # Todo: add is_active or is_working for us?
    # Todo: national_id, passport_id, passport_expire,


class Hire(models.Model):
    potential = models.BooleanField(verbose_name='is Potential?')
    interviewed = models.BooleanField(verbose_name='is Interviewed?')
    interview_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=64)
    firstname = models.CharField(max_length=128, null=True)
    lastname = models.CharField(max_length=128)
    phone = models.CharField(unique=True, help_text="+989125558877", max_length=64)
    skills = models.ManyToManyField(Skill)
    positions = models.ManyToManyField(Position, verbose_name="Potential Positions")
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    currency = models.ForeignKey('financial.Currency', related_name='hire_currency', null=True, blank=False,
                                 on_delete=models.CASCADE)
    min_salary = models.IntegerField(blank=True, null=True, verbose_name="Minimum Salary", help_text="per hour")
    max_salary = models.IntegerField(blank=True, null=True, verbose_name="Maximum Salary", help_text="per hour")
    attach = models.FileField(upload_to=upload_file_path, null=True, blank=True, help_text="Like resume and CV")
    notes = HTMLField(null=True, blank=True, help_text="you can write things who happened in interview")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    # todo: hire or not?, accept or not?, is_done?


# delete attach file after model has been deleted
@receiver(post_delete, sender=Hire)
def post_save_expense(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.attach.delete(save=False)
    except:
        pass


# update attach file after model has been updated
@receiver(pre_save, sender=Hire)
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
