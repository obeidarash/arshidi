# Generated by Django 4.1.1 on 2022-12-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0056_remove_project_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='source',
            field=models.CharField(choices=[('upwork', 'UpWork'), ('freelancer', 'Freelancer'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn')], default=('upwork', 'UpWork'), max_length=32),
        ),
    ]
