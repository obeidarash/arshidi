# Generated by Django 4.1.1 on 2022-12-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0055_alter_timesheet_payment_fixed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='fee',
        ),
    ]
