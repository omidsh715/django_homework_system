from django.contrib.auth.forms import UserCreationForm
from .models import MyCustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyCustomUser
        fields = ('username', 'password1', 'password2',)

