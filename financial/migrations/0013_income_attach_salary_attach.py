# Generated by Django 4.1.1 on 2022-10-24 21:39

from django.db import migrations, models
import financial.models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0012_alter_expense_attach'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to=financial.models.upload_file_path),
        ),
        migrations.AddField(
            model_name='salary',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to=financial.models.upload_file_path),
        ),
    ]
