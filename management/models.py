from django.db import models
from tinymce.models import HTMLField

STATUS = [
    ('start', 'Start'),
    ('finished', 'Finished'),
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


class Freelancer(models.Model):  # Todo: Think more about the name
    firstname = models.CharField(max_length=128, null=True)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(unique=True, help_text="+989125558877", max_length=64, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, help_text="What kind of skills this Freelancer has?")
    positions = models.ManyToManyField(Position, help_text="What kind of Position this Freelancer has?")
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Project(models.Model):
    title = models.CharField(max_length=512, help_text='Project name or title')
    link = models.URLField(null=True, blank=True)
    freelancers = models.ManyToManyField(Freelancer, help_text="which people work on this project?")
    skills = models.ManyToManyField(Skill, help_text="What kind of skills this project need?")
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=128)
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: date, freelancer, Duration, fixed price or not and ETC (Check upWork and freelancer),
    # Todo: Category, (in progress or finish, just start)

    def __str__(self):
        return self.title
