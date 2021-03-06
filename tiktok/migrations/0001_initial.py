# Generated by Django 4.0.6 on 2022-07-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('videoUrl', models.CharField(max_length=500)),
                ('videoDownloadUrl', models.CharField(max_length=500)),
                ('downloadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
