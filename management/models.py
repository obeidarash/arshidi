from django.db import models
from tinymce.models import HTMLField
from human_resources.models import Skill, Position, Employee

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


class Project(models.Model):
    title = models.CharField(max_length=512, help_text='Project name or title')
    term = models.CharField(choices=TERM, default=TERM[0], max_length=256)
    project_type = models.CharField(choices=TYPE, default=TERM[0], max_length=256)
    budget_type = models.CharField(choices=BUDGET, default=BUDGET[0], max_length=256)
    fixed_budget = models.IntegerField(default=0, null=True, blank=True)
    min_budget = models.IntegerField(default=0, null=True, blank=True, verbose_name='Min pay / hour',
                                     help_text="Minimum price per hour work")
    max_budget = models.IntegerField(default=0, null=True, blank=True, verbose_name='max pay / hour',
                                     help_text="Maximum price per hour work")
    people = models.IntegerField(default=1, help_text="How many people this project need?")
    employees = models.ManyToManyField(Employee, help_text="which people work on this project?")
    skills = models.ManyToManyField(Skill, help_text="What kind of skills this project need?")
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=128)
    link = models.URLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: date, freelancer, Duration, fixed price or not and ETC (Check upWork and freelancer),
    # Todo: Category, (in progress or finish, just start)
    # Todo: connect to contact and company
    # Todo: more than one freelancer??

    def __str__(self):
        return self.title


class TimeSheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # time = models.TimeField(null=True, blank=True)
    hour_work = models.CharField(help_text="Hour work - like 07:50 -> 7.5", max_length=4)
    date = models.DateField()
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + ": " + str(self.project) + " - " + str(self.employee)
