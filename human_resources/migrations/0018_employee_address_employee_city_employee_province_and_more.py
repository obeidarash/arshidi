# Generated by Django 4.1.1 on 2022-10-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0017_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='province',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='zipcode',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
