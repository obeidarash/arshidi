# Generated by Django 4.1.1 on 2022-10-24 16:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0010_alter_hire_interviewed_alter_hire_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Mr', 'Mr'), ('Ms', 'Ms')], max_length=64)),
                ('firstname', models.CharField(max_length=128, null=True)),
                ('lastname', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, help_text='+989125558877', max_length=64, null=True, unique=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='positions',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='skills',
        ),
        migrations.AlterField(
            model_name='hire',
            name='positions',
            field=models.ManyToManyField(help_text='What kind of Position this Employee has?', to='human_resources.position'),
        ),
        migrations.AlterField(
            model_name='hire',
            name='skills',
            field=models.ManyToManyField(help_text='What kind of skills this Employee has?', to='human_resources.skill'),
        ),
    ]
