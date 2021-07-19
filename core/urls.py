from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('student_upload/',views.student_upload, name="student_upload"),
    path('teacher_upload/', views.teacher_upload, name='teacher_upload'),
    path('success/', views.index, name='success'),
    path('', views.index, name='index'),
    path('homework_list', views.homework_list, name='homework_list'),
    path('homework_detail/<int:pk>/', views.student_upload, name='student_upload')
]
