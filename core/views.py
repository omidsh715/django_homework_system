from django.shortcuts import render, redirect
from .forms import TeacherFile, StudentFile
from django.contrib.auth.decorators import login_required
from .models import HomeWorks
from .models import HomeWorks
# Create your views here.

# todo 1 : download homework quiz for student
# todo 2 : teacher can see the student's uploads


def index(request):
    return render(request, 'index.html')


@login_required
def homework_list(request):
    homeworks = HomeWorks.objects.filter(student=request.user)
    context = {'homeworks':homeworks}
    return render(request,'homework_list.html', context=context)


@login_required
def teacher_upload(request):
    if request.user.user_type == 2:
        if request.method == "POST":
            form = TeacherFile(request.POST, request.FILES)
            if form.is_valid:
                post = form.save(commit=False)
                post.teacher = request.user
                post.save()
                return redirect('core:success')
        else:
            form = TeacherFile()
            context = {'form': form}
            return render(request, 'teacher_upload.html', context)


@login_required
def student_upload(request, pk):
    if request.user.user_type == 1:
        if request.method == "POST":
            form = StudentFile(request.POST, request.FILES)
            if form.is_valid:
                post = form.save(commit=False)
                post.student = request.user
                post.homework = HomeWorks.objects.get(pk=pk)
                post.save()
                return redirect('core:success')
        else:
            form = StudentFile()
            context = {'form': form}
            return render(request, 'student_upload.html', context)

