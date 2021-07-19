from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('student_upload/',views.student_upload, name="student_upload"),
    path('teacher_upload/', views.teacher_upload, name='teacher_upload'),
    path('success/', views.index, name='success'),
]
