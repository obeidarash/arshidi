# Generated by Django 4.1.1 on 2022-10-25 08:23

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0024_alter_hire_max_salary_alter_hire_min_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]