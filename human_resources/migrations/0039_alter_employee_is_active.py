# Generated by Django 4.1.1 on 2022-12-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0038_employee_national_id_employee_passport_expire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is this person currently active?'),
        ),
    ]