from django.db import models
from django.contrib.auth.models import AbstractUser


class MyCustomUser(AbstractUser):
    """
    this project has two types of users :
    1. student: they can access to homeworks that teachers allow them to answer
    2. teacher: they can create homeworks and set students that they want to answer the homeworks
    """
    user_type_choices = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=user_type_choices, default=1)
