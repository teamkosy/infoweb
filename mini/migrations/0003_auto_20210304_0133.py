# Generated by Django 3.1.5 on 2021-03-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0002_message_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='contents',
            field=models.TextField(help_text='내용을 입력해주세요~'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(help_text='최대 10자 내로 입력가능합니다.', max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(help_text='최대 50자 내로 입력가능합니다.', max_length=50),
        ),
    ]
