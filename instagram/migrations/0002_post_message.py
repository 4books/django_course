# Generated by Django 4.0.7 on 2022-10-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default='message'),
        ),
    ]
