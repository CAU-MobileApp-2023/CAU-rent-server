from django.db import models
from django.utils import timezone

# Create your models here.

class Device(models.Model):
    model_name = models.CharField(verbose_name='모델 이름', max_length=20)
    model_id = models.IntegerField(verbose_name='모델 번호')
    # is_available = models.BooleanField(verbose_name='대여 가능 여부')
    specification = models.TextField(verbose_name='설명(사양 등)', null=True, blank=True)

    class Meta:
        unique_together = ('model_name', 'model_id')

    def check_availability(self, start_date, end_date):
        from rental_records.models import DeviceRentalRecord 

        return not DeviceRentalRecord.objects.filter(
            device=self,
            start_date__lt=end_date,
            end_date__gt=start_date
        ).exists()

    def __str__(self):
        return f"{self.model_name}: {self.model_id}"