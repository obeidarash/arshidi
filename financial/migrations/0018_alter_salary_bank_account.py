# Generated by Django 4.1.1 on 2022-12-14 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0017_remove_income_paypal_delete_paypal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='bank_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.bankaccount', verbose_name='To bank account'),
        ),
    ]
