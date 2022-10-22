# Generated by Django 4.1.1 on 2022-10-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_alter_freelancer_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Web Developer or Front End Developer', max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='skills',
            field=models.ManyToManyField(help_text='What kind of skills this Freelancer has?', to='management.skill'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='position',
            field=models.ManyToManyField(help_text='What kind of Position this Freelancer has', to='management.position'),
        ),
    ]
