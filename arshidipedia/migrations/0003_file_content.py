# Generated by Django 4.1.1 on 2023-05-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arshidipedia', '0002_alter_library_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
