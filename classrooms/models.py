from django.db import models
from datetime import datetime

# Create your models here.

class Classroom(models.Model):
    building = models.CharField(verbose_name='건물 이름', max_length=20)
    room = models.CharField(verbose_name='강의실 이름', max_length=10)
    capacity = models.IntegerField(verbose_name='최대 수용 인원')
    # is_available = models.BooleanField(verbose_name='대여 가능 여부', default=True)

    class Meta:
        unique_together = ('building', 'room')

    def check_availability(self, check_date, start_time, end_time):
        from rental_records.models import ClassroomRentalRecord 

        start_datetime = datetime.combine(check_date, start_time)
        end_datetime = datetime.combine(check_date, end_time)

        # 해당 시간대에 대여 기록이 있는지 확인
        return not ClassroomRentalRecord.objects.filter(
            classroom=self,
            start_date__lt=end_datetime,
            end_date__gt=start_datetime
        ).exists()

    def __str__(self):
        return f"{self.building} {self.room}"