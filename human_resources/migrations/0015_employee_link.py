# Generated by Django 4.1.1 on 2022-10-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0014_remove_employee_birthday_remove_employee_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
