# Generated by Django 4.1.1 on 2022-10-22 20:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_project_skills_alter_skill_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
