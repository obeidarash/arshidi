# Generated by Django 4.1.1 on 2023-04-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arshidipedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='content',
            field=models.TextField(),
        ),
    ]
