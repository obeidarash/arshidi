# Generated by Django 4.1.1 on 2022-10-29 02:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('arshidipedia', '0011_alter_library_options_library_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]