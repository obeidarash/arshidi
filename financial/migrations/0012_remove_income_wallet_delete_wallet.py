# Generated by Django 4.1.1 on 2022-12-13 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0011_currency_crypto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='wallet',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
