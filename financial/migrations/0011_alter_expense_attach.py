# Generated by Django 4.1.1 on 2022-10-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0010_expense_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to='attach/'),
        ),
    ]