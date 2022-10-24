from django.db import models
from tinymce.models import HTMLField

GENDER = [
    ('Mr', 'Mr'),
    ('Ms', 'Ms')
]


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
    firstname = models.CharField(max_length=128, null=True)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, help_text="With dial code: +989125558877", max_length=64)
    birthday = models.DateField()
    skills = models.ManyToManyField(Skill)
    positions = models.ManyToManyField(Position)
    link = models.URLField(null=True, blank=True)
    # country = CountryField(blank_label='select country', null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gender + " " + self.firstname + " " + self.lastname


class Hire(models.Model):
    potential = models.BooleanField(verbose_name='is Potential?')
    interviewed = models.BooleanField(verbose_name='is Interviewed?')
    gender = models.CharField(choices=GENDER, max_length=64)
    firstname = models.CharField(max_length=128, null=True)
    lastname = models.CharField(max_length=128)
    birthday = models.DateField(null=True, blank=True)
    interview_date = models.DateField(null=True, blank=True)
    # email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(unique=True, help_text="+989125558877", max_length=64)
    skills = models.ManyToManyField(Skill, help_text="What kind of skills this Employee has?")
    positions = models.ManyToManyField(Position, help_text="What kind of Position this Employee has?")
    min_salary = models.IntegerField(blank=True, null=True, verbose_name="Minimum Salary (Toman)", help_text='per hour')
    max_salary = models.IntegerField(blank=True, null=True, verbose_name="Maximum Salary (Toman)", help_text='per hour')
    notes = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gender + " " + self.firstname + " " + self.lastname

    # todo:  file (resume), min and max salary per hour, accept or not
