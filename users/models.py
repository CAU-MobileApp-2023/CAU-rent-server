from django.db import models

# Create your models here.

class ServiceUser(models.Model):
    email = models.EmailField(verbose_name='이메일', unique=True)
    password = models.CharField(verbose_name='비밀번호', max_length=20)
    name = models.CharField(verbose_name='이름', max_length=30)
    student_id = models.CharField(verbose_name='학번', unique=True, max_length=8, primary_key=True)
    phone_number = models.CharField(verbose_name='전화번호', max_length=11)
    department = models.CharField(verbose_name='학과(부)', max_length=25)

    def __str__(self):
        return f"{self.name} {self.student_id}"