# Generated by Django 4.1.3 on 2022-11-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0016_salary_advance_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='advance_payment',
            field=models.BooleanField(default=False),
        ),
    ]
