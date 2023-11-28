from django.urls import path
from .views import UserList, UserDetail, UserSignUp, UserLogin, UserLogout

urlpatterns = [
    path('inform/', UserList.as_view()),
    path('inform/<str:student_id>/', UserDetail.as_view()),
    path('signup/', UserSignUp.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
]