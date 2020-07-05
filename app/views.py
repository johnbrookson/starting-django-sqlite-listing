from django.shortcuts import render

# Create your views here.
from app.models import Lesson


def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(
        request,
        'lesson_list.html',
        {
            'lessons': lessons
        }
    )
