# Generated by Django 4.1.1 on 2022-10-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0026_project_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('', '')], default=('short', 'Short-term or part-time work (Less than 30hr/week and less than 3 months)'), max_length=256),
        ),
    ]
