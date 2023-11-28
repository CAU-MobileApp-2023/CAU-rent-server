from django.urls import path
from .views import RentalRecordList, RentalRecordListByStudentId, RentDevice, RentClassroom

urlpatterns = [
    path('inform/', RentalRecordList.as_view()),
    path('inform/<str:student_id>/', RentalRecordListByStudentId.as_view()),
    path('rent/device/', RentDevice.as_view()),
    path('rent/classroom/', RentClassroom.as_view()),
]