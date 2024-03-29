# Generated by Django 4.1.1 on 2023-02-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0068_delete_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget_type',
            field=models.CharField(choices=[('hour', 'Pay by the hour'), ('fixed', 'Pay a fixed price')], default=('fixed', 'Pay a fixed price'), max_length=256),
        ),
    ]
