from django.db import models

class Member(models.Model):
    uid = models.CharField(max_length=20)
    upw = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, help_text='"-" 제외하고 입력해주세요.')
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uid
