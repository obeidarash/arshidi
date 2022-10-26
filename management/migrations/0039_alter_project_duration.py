# Generated by Django 4.1.1 on 2022-10-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0038_project_duration_alter_project_experience_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.CharField(choices=[('0', 'Less than 1 month'), ('1', 'More than 1 month'), ('2', '1 to 3 months'), ('3', '3 to 6 months'), ('4', 'More than 6 months')], default=('0', 'Less than 1 month'), max_length=256),
        ),
    ]
