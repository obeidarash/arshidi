# Generated by Django 4.1.1 on 2022-10-30 08:17

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_company_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='plate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='province',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='zipcode',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
