from django.db import models
from human_resources.models import GENDER
from tinymce.models import HTMLField


class Contact(models.Model):
    gender = models.CharField(choices=GENDER, max_length=16)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    comment = models.TextField(blank=True, null=True)

    # todo: hashtag
    # todo: add validator to first and lastname


class Company(models.Model):
    name = models.CharField(max_length=256)
    contact = models.ManyToManyField(Contact)
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    # country = CountryField(blank_label='select country', null=True, blank=True, verbose_name="کشور")
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    # plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
