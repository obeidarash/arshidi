from django.db import models
from tinymce.models import HTMLField
import financial.models
from human_resources.models import Skill, Position, Employee

CURRENCY = [
    ('USD', 'US Dollar'),
    ('USDT', 'Tether'),
    ('IRR', 'Rial'),
]

STATUS = [
    ('start', 'Start'),
    ('finished', 'Finished'),
]

TERM = [
    ('short', "Short-term or part-time work: Less than 30hr/week and less than 3 months"),
    ('long', "Long-term work: More than 30 hrs/week and more than 3 months")
]

TYPE = [
    ('onetime', 'One-time project'),
    ('ongoing', 'Ongoing project'),
    ('complex', 'Complex project'),
]

BUDGET = [
    ('hour', 'Pay by the hour'),
    ('fixed', 'Pay a fixed price'),
]

EXPERIENCE = [
    ('expert', 'Expert'),
    ('intermediate', 'Intermediate'),
    ('beginner', 'Beginner'),
]

DURATION = [
    ('0', 'Less than 1 month'),
    ('1', 'More than 1 month'),
    ('2', '1 to 3 months'),
    ('3', '3 to 6 months'),
    ('4', 'More than 6 months'),
]


class Project(models.Model):
    title = models.CharField(max_length=512, help_text='Project name or title')
    term = models.CharField(choices=TERM, default=TERM[0], max_length=256)
    project_type = models.CharField(choices=TYPE, default=TERM[0], max_length=256)
    experience_level = models.CharField(choices=EXPERIENCE, default=EXPERIENCE[0], max_length=256)
    duration = models.CharField(choices=DURATION, default=DURATION[0], max_length=256)
    budget_type = models.CharField(choices=BUDGET, default=BUDGET[0], max_length=256)
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=256)
    fixed_budget = models.IntegerField(default=0, null=True, blank=True)
    min_budget = models.IntegerField(default=0, null=True, blank=True, verbose_name='Min pay / hour',
                                     help_text="Minimum price per hour work")
    max_budget = models.IntegerField(default=0, null=True, blank=True, verbose_name='max pay / hour',
                                     help_text="Maximum price per hour work")
    people = models.IntegerField(default=1, help_text="How many people this project need?")
    employees = models.ManyToManyField(Employee, help_text="which people work on this project?", blank=True)
    skills = models.ManyToManyField(Skill, help_text="What kind of skills this project need?")
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=128)
    link = models.URLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: date, Duration, fixed price or not and ETC (Check upWork and freelancer),
    # Todo: Category, (in progress or finish, just start)
    # Todo: connect to contact and company

    def __str__(self):
        return self.title


class TimeSheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hour_work = models.CharField(help_text="Hour work - like 07:50 -> 7.5", max_length=4)
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=64)
    price = models.BigIntegerField(help_text='hourly price for working on this project')
    date = models.DateField()
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + ": " + str(self.project) + " - " + str(self.employee)
