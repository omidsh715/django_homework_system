from django.db import models
from django.contrib.auth.models import AbstractUser


class MyCustomUser(AbstractUser):
    user_type_choices = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=user_type_choices, default=1)
