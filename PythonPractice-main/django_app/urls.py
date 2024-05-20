from django.urls import path
from .views import *

urlpatterns = [
    path('django_library/', django_library, name='django_library'),
    path('django_orm/', django_orm, name='django_orm'),
    path('django_testing/', django_testing, name='django_testing'),
    path('django_interview_questions/', django_interview_questions,
         name='django_interview_questions'),
    path('django_rest_framework/', django_rest_framework, name="django_rest_framework"),
    path('django_rest_framework_details/', django_rest_framework_details, name="django_rest_framework_details"),

]
