from django.db import models
from tinymce.models import HTMLField
from human_resources.models import Skill, Position, Freelancer

STATUS = [
    ('start', 'Start'),
    ('finished', 'Finished'),
]


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


class TimeSheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    # time = models.TimeField(null=True, blank=True)
    date = models.DateField()
    description = HTMLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + ": " + str(self.project) + " - " + str(self.freelancer)
