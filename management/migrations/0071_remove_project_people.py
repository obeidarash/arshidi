# Generated by Django 4.1.1 on 2023-02-24 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0070_alter_project_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='people',
        ),
    ]
