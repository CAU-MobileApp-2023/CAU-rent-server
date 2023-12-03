from django.urls import path
from .views import *

urlpatterns = [
    path('rent/device/', RentDevice.as_view()),                                                     # 특정 장치 대여
    path('rent/classroom/', RentClassroom.as_view()),                                               # 특정 강의실 대여    
    path('devices/', DeviceRentalRecordList.as_view()),                                             # 모든 장치의 대여 정보
    path('classrooms/', ClassroomRentalRecordList.as_view()),                                       # 모든 강의실의 대여 정보
    path('device/<str:model_name>/<str:model_id>/', RentalRecordListOfDevice.as_view()),            # 특정 장치의 대여 정보
    path('classroom/<str:building>/<str:room>/', RentalRecordListOfClassroom.as_view()),            # 특정 강의실의 대여 정보    
    path('devices/<str:student_id>/', DeviceRentalRecordListByStudentId.as_view()),                 # 특정 학생의 장치 대여 정보
    path('classrooms/<str:student_id>/', ClassroomRentalRecordListByStudentId.as_view()),           # 특정 학생의 강의실 대여 정보
    path('classrooms/<str:student_id>/now/', NowClassroomRentalRecordListByStudentId.as_view()),    #  
    path('devices/<str:student_id>/now/', NowDeviceRentalRecordListByStudentId.as_view()),          # 
]