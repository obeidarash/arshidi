# Generated by Django 4.1.3 on 2022-11-15 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arshidipedia', '0014_alter_library_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='SEO, models and etc', max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='library',
            name='category',
        ),
        migrations.AddField(
            model_name='library',
            name='category',
            field=models.ManyToManyField(to='arshidipedia.category'),
        ),
    ]
