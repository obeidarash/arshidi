# Generated by Django 4.1.1 on 2022-10-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0012_delete_freelancer_employee_positions_employee_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=1, help_text='+989125558877', max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
