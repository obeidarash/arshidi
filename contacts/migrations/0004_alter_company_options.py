# Generated by Django 4.1.1 on 2022-10-24 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_company_alter_contact_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
    ]
