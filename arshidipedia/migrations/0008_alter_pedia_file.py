# Generated by Django 4.1.1 on 2022-10-29 02:08

import arshidipedia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arshidipedia', '0007_pedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedia',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=arshidipedia.models.upload_file_path),
        ),
    ]