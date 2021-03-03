from django.db import models
from django.utils import timezone
from django.urls import reverse

class Message(models.Model):
    title = models.CharField(max_length=50,help_text='최대 50자 내로 입력가능합니다.')
    name = models.CharField(max_length=10,help_text='최대 10자 내로 입력가능합니다.')
    contents = models.TextField(help_text='내용을 입력해주세요~')
    regdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view', args=[str(self.id)])

