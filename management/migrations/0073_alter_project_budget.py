# Generated by Django 4.1.1 on 2023-05-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0072_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.FloatField(default=0),
        ),
    ]
