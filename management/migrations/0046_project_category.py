# Generated by Django 4.1.1 on 2022-10-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0045_project_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('programming', 'Programming'), ('seo', 'SEO')], default=('programming', 'Programming'), max_length=256),
        ),
    ]