from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HomeWorks(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 2})
    student = models.ManyToManyField(User, limit_choices_to={'user_type': 1})
    is_enable = models.BooleanField(default=True)
    def __str__(self):
        return '{}'.format(self.title)

class HomeWorkUpload(models.Model):
    homework = models.ManyToManyField(HomeWorks, limit_choices_to={"is_enable": True})
    file = models.FileField(upload_to='')
    def __str__(self):
        return '{}'.format(self.homework)


class Results(models.Model):
    homework = models.ManyToManyField(HomeWorks, limit_choices_to={'is_enable': True})
    score = models.PositiveSmallIntegerField()
    def __str__(self):
        return '{}'.format(self.homework)
