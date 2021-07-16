from django.db import models
from homework.settings import AUTH_USER_MODEL
# Create your models here.


class HomeWorks(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploaded_files/teachers_quiz/")
    teacher = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 2},
                                related_name='teacher_user')

    student = models.ManyToManyField(AUTH_USER_MODEL, limit_choices_to={'user_type': 1},
                                     related_name='student_user')

    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.title)


class HomeWorkUpload(models.Model):
    homework = models.ManyToManyField(HomeWorks, limit_choices_to={"is_enable": True})
    file = models.FileField(upload_to='uploaded_files/students_answers/')
    student = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 1},
                                related_name='student_user_upload')
    def __str__(self):
        return '{}'.format(self.homework)


class Results(models.Model):
    homework = models.ManyToManyField(HomeWorks, limit_choices_to={'is_enable': True})
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}'.format(self.homework)
