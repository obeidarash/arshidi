# Generated by Django 4.1.1 on 2022-11-07 01:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0032_employee_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, help_text='you can write things who happened in interview', null=True),
        ),
    ]
