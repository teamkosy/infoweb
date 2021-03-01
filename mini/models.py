from django.db import models
from datetime import datetime

class Message(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    contents = models.TextField()
    regdate = datetime.now()

    def __str__(self):
        return self.title
