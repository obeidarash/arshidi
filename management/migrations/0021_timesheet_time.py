# Generated by Django 4.1.1 on 2022-10-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_timesheet_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
