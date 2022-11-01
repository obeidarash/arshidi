# Generated by Django 4.1.1 on 2022-11-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0018_tag_company_created_company_updated_contact_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='contacts.tag'),
        ),
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='contacts.tag'),
        ),
    ]
