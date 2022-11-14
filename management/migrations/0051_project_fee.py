# Generated by Django 4.1.3 on 2022-11-12 08:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0050_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='fee',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
