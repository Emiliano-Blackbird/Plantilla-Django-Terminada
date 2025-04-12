# Create your views here.
from django.shortcuts import render

from courses.models import Course
from blog.models import Post
from .forms import ContactForms


# Vistas generales de la app
def home(request):

    context = {
        'courses': Course.objects.filter(show_home=True),
        'posts': Post.objects.filter(show_home=True),
    }
    return render(request, 'core/home.html', context)


def about_us(request):
    return render(request, 'core/about_us.html')


def login(request):
    return render(request, 'core/login.html')


def register(request):
    return render(request, 'core/register.html')


def contact(request):
    if request.POST:
        formulario = ContactForms(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            print(f"Se ha enviado un correo a {nombre} procedente de email {email} con el texto {comentario}")
            context = {
                "form": formulario,
                "success": True
            }
            return render(request, "core/contact.html", context)
        else:
            context = {
                "form": formulario,
            }
            return render(request, "core/contact.html", context)

    formulario = ContactForms()
    context = {
        "form": formulario,
    }
    return render(request, "core/contact.html", context)
