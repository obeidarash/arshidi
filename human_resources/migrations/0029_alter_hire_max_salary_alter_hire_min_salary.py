# Generated by Django 4.1.1 on 2022-10-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0028_alter_hire_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='max_salary',
            field=models.IntegerField(blank=True, help_text='per hour', null=True, verbose_name='Maximum Salary'),
        ),
        migrations.AlterField(
            model_name='hire',
            name='min_salary',
            field=models.IntegerField(blank=True, help_text='per hour', null=True, verbose_name='Minimum Salary'),
        ),
    ]
