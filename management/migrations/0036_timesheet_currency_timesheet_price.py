# Generated by Django 4.1.1 on 2022-10-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0035_alter_project_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='currency',
            field=models.CharField(choices=[('IRR', 'Rial'), ('USD', 'US Dollar'), ('USDT', 'Tether')], default=('IRR', 'Rial'), max_length=64),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='price',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]