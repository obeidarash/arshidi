# Generated by Django 4.1.1 on 2022-10-28 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0041_alter_project_currency_alter_timesheet_currency'),
        ('financial', '0009_expense_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='project',
            field=models.ManyToManyField(blank=True, related_name='salary_project', to='management.project', verbose_name='Project(s)'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense_project', to='management.project'),
        ),
    ]
