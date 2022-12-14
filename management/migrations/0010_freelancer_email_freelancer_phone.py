# Generated by Django 4.1.1 on 2022-10-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_freelancer_created_freelancer_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='email',
            field=models.EmailField(default=0, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freelancer',
            name='phone',
            field=models.CharField(default=0, help_text='+989125558877', max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
