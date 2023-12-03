from django.db import models
from users.models import ServiceUser
from devices.models import Device
from classrooms.models import Classroom

# Create your models here.

class DeviceRentalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    renter = models.ForeignKey(ServiceUser, verbose_name='대여자', on_delete=models.CASCADE)
    device = models.ForeignKey(Device,verbose_name='대여한 장치', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(verbose_name='대여 시작 정보')
    end_date = models.DateTimeField(verbose_name='대여 반납 정보')

    def __str__(self):
        return f"대여자: {self.renter}, 대여 항목: {self.device}"


class ClassroomRentalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    renter = models.ForeignKey(ServiceUser, verbose_name='대여자', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, verbose_name='대여한 강의실', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(verbose_name='대여 시작 정보')
    end_date = models.DateTimeField(verbose_name='대여 반납 정보')

    def __str__(self):
        return f"대여자: {self.renter}, 대여 항목: {self.classroom}"