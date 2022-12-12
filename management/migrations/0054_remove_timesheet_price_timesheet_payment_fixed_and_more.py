# Generated by Django 4.1.3 on 2022-11-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0053_timesheet_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='price',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='payment_fixed',
            field=models.BigIntegerField(blank=True, help_text='hourly price for working on this project', null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='payment_hourly',
            field=models.BigIntegerField(blank=True, help_text='hourly price for working on this project', null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='payment_type',
            field=models.CharField(choices=[('hour', 'Pay by the hour'), ('fixed', 'Pay a fixed price')], default=('hour', 'Pay by the hour'), help_text='How you pay employee', max_length=256),
        ),
    ]