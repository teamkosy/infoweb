# Generated by Django 3.1.5 on 2021-03-01 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='regdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
