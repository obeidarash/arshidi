# Generated by Django 4.1.1 on 2022-10-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_skill_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
