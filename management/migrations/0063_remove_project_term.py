# Generated by Django 4.1.1 on 2022-12-11 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0062_remove_project_project_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='term',
        ),
    ]