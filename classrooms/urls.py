from django.urls import path
from .views import *

urlpatterns = [
    path('inform/', ClassroomList.as_view()),
    path('inform/<str:building>/', ClassroomListInBuilding.as_view()),
    path('inform/<str:building>/<str:room>/', ClassroomDetail.as_view()),
    path('register/', ClassroomRegister.as_view()),
    path('availability/<str:building>/<str:room>/<str:check_date>/', ClassroomAvailability.as_view()),
]