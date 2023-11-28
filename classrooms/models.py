from django.db import models

# Create your models here.

class Classroom(models.Model):
    building = models.CharField(verbose_name='건물 이름', max_length=20)
    room = models.CharField(verbose_name='강의실 이름', max_length=10)
    capacity = models.IntegerField(verbose_name='최대 수용 인원')
    is_available = models.BooleanField(verbose_name='대여 가능 여부', default=True)

    class Meta:
        unique_together = ('building', 'room')

    def __str__(self):
        return f"{self.building} {self.room}"