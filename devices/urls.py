from django.urls import path
from .views import *

urlpatterns = [
    path('inform/', DeviceList.as_view()),
    path('inform/<str:model_name>/', DeviceListByModelName.as_view(), name='device-by-model-name'),
    path('inform/<str:model_name>/<int:model_id>/', DeviceDetail.as_view(), name='single-device'),    
    path('register/', DeviceRegister.as_view()),
    path('availability/<str:model_name>/<int:model_id>/', DeviceAvailability.as_view(), name='device-availability'),
]