# Generated by Django 4.1.1 on 2022-12-11 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.currency'),
        ),
    ]
