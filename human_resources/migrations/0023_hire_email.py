# Generated by Django 4.1.1 on 2022-10-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0022_employee_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]