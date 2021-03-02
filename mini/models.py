from django.db import models
from django.utils import timezone

class Message(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    contents = models.TextField()
    regdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
