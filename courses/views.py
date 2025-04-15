# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Course


# Vistas generales de la app
@login_required  # Decorador para requerir login
def course_list(request):
    courses = Course.objects.all()  # Todos los cursos de la base de datos
    context = {
        'courses': courses
    }
    return render(request, 'courses/course_list.html', context)


@login_required  # Decorador para requerir login
def course_detail(request, id):
    course = Course.objects.get(pk=id)  # Obtener el curso por su id
    context = {
        'course': course
    }
    return render(request, 'courses/course_detail.html', context)
