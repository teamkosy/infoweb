from django.db import models

class Album(models.Model):
    a_no = models.AutoField(primary_key=True)
    a_type = models.CharField(max_length=50)
    a_title = models.CharField(max_length=255)
    a_note = models.CharField(max_length=4096)
    a_image = models.CharField(max_length=1000)
    a_count = models.IntegerField(default=0)
    a_datetime = models.DateTimeField(auto_now=True)
    a_usage = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'album'

    def __str__(self):
        return "제목 : " + self.a_title + ", 유형 : " + self.a_type