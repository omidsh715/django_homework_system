from django import forms
from .models import HomeWorks, HomeWorkUpload


class TeacherFile(forms.ModelForm):
    """
    form for uploading quiz by teachers and create HomeWork objects
    NOTE : teacher field will automatically fill with "request.user" objects in view
    """
    class Meta:
        model = HomeWorks
        fields = ('file', 'title', 'student')


class StudentFile(forms.ModelForm):
    """
    form for students that can upload their answers
    NOTE : student field will be automatically fill with "request.user" objects in view
     """
    class Meta:
        model = HomeWorkUpload
        fields = ('file',)
