from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    # date = now()

    def __str__(self):
        return self.title
