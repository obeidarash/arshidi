from django.db import models
from tinymce.models import HTMLField
from human_resources.models import Skill, Position, Employee
from contacts.models import Contact, Company
from timezone_field import TimeZoneField
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

CURRENCY = [
    ('USD', 'US Dollar'),
    ('USDT', 'Tether'),
    ('IRR', 'Rial'),
]

CATEGORY = [
    ('programming', 'Programming'),
    ('wordpress', 'Wordpress'),
    ('seo', 'SEO'),
]

STATUS = [
    ('upcoming', 'Upcoming'),
    ('not-started', 'Not started'),
    ('active', 'Active'),
    ('overdue', 'Overdue'),
    ('pending', 'Pending'),
    ('canceled', 'Canceled'),
    ('priority', 'Priority'),
    ('completed', 'Completed'),
]

# TERM = [
#     ('short', "Short-term or part-time work: Less than 30hr/week and less than 3 months"),
#     ('long', "Long-term work: More than 30 hrs/week and more than 3 months")
# ]

# TYPE = [
#     ('onetime', 'One-time project'),
#     ('ongoing', 'Ongoing project'),
#     ('complex', 'Complex project'),
# ]

BUDGET = [
    ('hour', 'Pay by the hour'),
    ('fixed', 'Pay a fixed price'),
]

DURATION = [
    ('0', 'Less than 1 month'),
    ('1', 'More than 1 month'),
    ('2', '1 to 3 months'),
    ('3', '3 to 6 months'),
    ('4', 'More than 6 months'),
]
SOURCE = [
    ('upwork', 'UpWork'),
    ('freelancer', 'Freelancer'),
    ('facebook', 'Facebook'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),
    ('website', 'Website'),
    ('direct', 'Direct'),
]


class Category(models.Model):
    title = models.CharField(max_length=128, help_text="SEO or WordPress", unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Project(models.Model):
    payment = models.BooleanField(help_text="is payment complete?", default=False)
    title = models.CharField(max_length=512, help_text='Project name or title', verbose_name="Name")
    Category = models.ManyToManyField(Category, blank=False)
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=128,
                              help_text="https://www.indeed.com/career-advice/career-development/project-statuses")
    # term = models.CharField(choices=TERM, default=TERM[0], max_length=256)
    source = models.CharField(choices=SOURCE, default=SOURCE[0], max_length=32)
    duration = models.CharField(choices=DURATION, default=DURATION[0], max_length=256)
    # project_type = models.CharField(choices=TYPE, default=TYPE[0], max_length=256)
    currency = models.CharField(choices=CURRENCY, default=CURRENCY[0], max_length=256)
    budget_type = models.CharField(choices=BUDGET, default=BUDGET[0], max_length=256)
    budget = models.IntegerField(default=0, null=False, blank=False)
    estimation = models.BooleanField(help_text="Is this budget an estimation?", default=False)
    people = models.IntegerField(default=1, help_text="How many people this project need?")
    skills = models.ManyToManyField(Skill, help_text="What kind of skills this project need?")
    country = CountryField(blank_label="Select Country", blank=True, null=True)
    timezone = TimeZoneField(choices_display="WITH_GMT_OFFSET", blank=True, null=True, help_text="Client Timezone")
    deadline = models.DateField(null=True, blank=True)
    employees = models.ManyToManyField(Employee, help_text="which people work on this project?", blank=True,
                                       verbose_name="Employee(s)")
    company = models.ForeignKey(Company, related_name="project_company", on_delete=models.CASCADE, blank=True,
                                null=True)
    contact = models.ManyToManyField(Contact, related_name="project_contact", blank=True, verbose_name="Contact(s)",
                                     help_text="Who are we in touch with in this project?")
    link = models.URLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True,
                            help_text="you can write project agreement, duties or salary of each person or any other "
                                      "thing")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Todo: date,  or not and ETC (Check upWork and freelancer),
    # Todo: (Phase): plan, build and implement, transition & close, completed
    # Todo: contract signed date
    # Todo: do something about price

    def __str__(self):
        return self.title

