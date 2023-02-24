# Generated by Django 4.1.1 on 2023-02-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0022_contact_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='facebook',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='instagram',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='linkedin',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='telegram',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='twitter',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='WhatsApp'),
        ),
        migrations.AddField(
            model_name='company',
            name='youtube',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
