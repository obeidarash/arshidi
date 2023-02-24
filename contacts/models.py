from django.db import models
from human_resources.models import GENDER
from django_countries.fields import CountryField


class Tag(models.Model):
    title = models.CharField(max_length=128, help_text="Client or Supplier", unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    gender = models.CharField(choices=GENDER, max_length=16)
    tags = models.ManyToManyField(Tag, blank=True)
    firstname = models.CharField(max_length=128, blank=True, null=True)
    lastname = models.CharField(max_length=128, blank=True, null=True)
    middlename = models.CharField(max_length=128, blank=True, null=True)
    nickname = models.CharField(max_length=128, blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)
    # Contact
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    # Address
    country = CountryField(blank_label='Select Country', null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)
    # Social Media
    linkedin = models.CharField(max_length=512, null=True, blank=True)
    facebook = models.CharField(max_length=512, null=True, blank=True)
    instagram = models.CharField(max_length=512, null=True, blank=True)
    twitter = models.CharField(max_length=512, null=True, blank=True)
    youtube = models.CharField(max_length=512, null=True, blank=True)
    telegram = models.CharField(max_length=512, null=True, blank=True)
    whatsapp = models.CharField(max_length=512, null=True, blank=True, verbose_name="WhatsApp")

    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        if self.firstname and self.lastname:
            return self.firstname + " " + self.lastname
        if not self.firstname and self.lastname:
            return self.lastname
        if self.firstname and not self.lastname:
            return self.firstname


class Company(models.Model):
    name = models.CharField(max_length=256)
    contact = models.ManyToManyField(Contact, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    # Contact
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    # Address
    country = CountryField(blank_label='Select Country', null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    plate = models.IntegerField(null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)
    # Social Media
    linkedin = models.CharField(max_length=512, null=True, blank=True)
    facebook = models.CharField(max_length=512, null=True, blank=True)
    instagram = models.CharField(max_length=512, null=True, blank=True)
    twitter = models.CharField(max_length=512, null=True, blank=True)
    youtube = models.CharField(max_length=512, null=True, blank=True)
    telegram = models.CharField(max_length=512, null=True, blank=True)
    whatsapp = models.CharField(max_length=512, null=True, blank=True, verbose_name="WhatsApp")

    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
