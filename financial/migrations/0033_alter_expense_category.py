# Generated by Django 4.1.1 on 2023-02-25 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0032_remove_income_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(blank=True, help_text='https://www.brex.com/journal/business-expense-categories', null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.category'),
        ),
    ]
