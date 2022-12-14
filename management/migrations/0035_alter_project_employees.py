# Generated by Django 4.1.1 on 2022-10-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0025_employee_country'),
        ('management', '0034_alter_project_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(blank=True, help_text='which people work on this project?', to='human_resources.employee'),
        ),
    ]
