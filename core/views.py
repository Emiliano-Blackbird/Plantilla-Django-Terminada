# Create your views here.
from django.shortcuts import render

from courses.models import Course
from blog.models import Post
from .forms import ContactForms
from django.core.mail import send_mail
from .models import Contact  # En caso de fallo del mail


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

# Configurar en settings.py el email de host para utilizar estas funciones
            message_content = f"{nombre} con email {email} ha enviado el siguiente mensaje: {comentario}"

            Contact.objects.create(
                nombre=nombre,
                email=email,
                comentario=comentario
            )

            success = send_mail(
                "Formulario de contacto de mi Web",
                message_content,
                "email del host que utilicé en settings.py",
                ["email de usuario que utilicé en settings.py"],
                fail_silently=False,
            )

            context = {
                "form": formulario,
                "success": success,
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
