from django.urls import path
from .views import DeviceList, DeviceListByModelName, DeviceDetail, DeviceRegister

urlpatterns = [
    path('inform/', DeviceList.as_view()),
    path('inform/<str:model_name>/', DeviceListByModelName.as_view(), name='device-by-model-name'),
    path('inform/<str:model_name>/<int:model_id>/', DeviceDetail.as_view(), name='single-device'),    
    path('register/', DeviceRegister.as_view()),
]