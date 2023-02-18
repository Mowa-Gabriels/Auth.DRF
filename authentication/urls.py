
from django.urls import path
from .views import (TeacherRegisterView, StudentRegisterView,
                    TeacherVerifyEmailView,
                    StudentVerifyEmailView, 
                    LoginAPIView, PasswordTokenCheckAPIView,
                      RequestPasswordReset, SetNewPasswordAPIView)
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [

   path('register/teacher-account', TeacherRegisterView.as_view(), name='register'),
   path('register/student-account', StudentRegisterView.as_view(), name='register'),


   path('verify-email/teacher', TeacherVerifyEmailView.as_view(), name='verify-email-teacher'), 
   path('verify-email/student', StudentVerifyEmailView.as_view(), name='verify-email-student'), 

   path('login/', LoginAPIView.as_view(), name='login'),  


   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('api/request-rest-email/', RequestPasswordReset.as_view(),
         name='request-rest-email'),
   
   path('api/password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(),
         name='password-reset-confirm'),

   path('api/password-reset/complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
         
]

