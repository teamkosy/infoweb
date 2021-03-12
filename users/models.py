from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
