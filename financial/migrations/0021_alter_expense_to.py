# Generated by Django 4.1.1 on 2023-02-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0022_contact_position'),
        ('financial', '0020_remove_income_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='to',
            field=models.ForeignKey(help_text='UpWork, Uber ETC', null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.company'),
        ),
    ]