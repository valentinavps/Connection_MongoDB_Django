# Generated by Django 5.0.5 on 2024-05-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_poc_currenttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poc',
            name='currentTime',
            field=models.CharField(default=0, max_length=180),
        ),
    ]
