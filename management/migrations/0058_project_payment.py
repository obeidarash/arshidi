# Generated by Django 4.1.1 on 2022-12-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0057_project_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='payment',
            field=models.BooleanField(default=False, help_text='is payment complete?'),
        ),
    ]
