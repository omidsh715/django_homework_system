from django.shortcuts import render, redirect
from .forms import TeacherFile, StudentFile
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')

# todo there is no attribute named is_teacher or is_student
@login_required
def teacher_upload(request):
    if request.user.user_type == 2:
        if request.method == "POST":
            form = TeacherFile(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                return redirect('core:success')
        else:
            form = TeacherFile()
            context = {'form': form}
            return render(request, 'teacher_upload.html', context)


@login_required
def student_upload(request):
    if request.user.user_type == 1:
        if request.method == "POST":
            form = StudentFile(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                return redirect('core:success')
        else:
            form = StudentFile()
            context = {'form': form}
            return render(request, 'student_upload.html', context)
