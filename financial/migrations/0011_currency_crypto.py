# Generated by Django 4.1.1 on 2022-12-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0010_alter_wallet_address_alter_wallet_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='crypto',
            field=models.BooleanField(default=False),
        ),
    ]
