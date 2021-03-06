# Generated by Django 3.1.5 on 2021-03-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='최대 50자 내로 입력가능합니다.', max_length=50)),
                ('name', models.CharField(help_text='최대 10자 내로 입력가능합니다.', max_length=10)),
                ('contents', models.TextField(default='', help_text='내용을 입력해주세요~')),
                ('regdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
