# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from courses.models import Course
from blog.models import Post
from .forms import ContactForms, LoginForm
from django.core.mail import send_mail
from .models import Contact  # En caso de fallo del mail
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout


# Vistas generales de la app
def home(request):

    context = {
        'courses': Course.objects.filter(show_home=True),
        'posts': Post.objects.filter(show_home=True),
    }
    return render(request, 'core/home.html', context)


def about_us(request):
    return render(request, 'core/about_us.html')


def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': 'Usuario no valido',
                }
                return render(request, 'core/login.html', context)
        else:
            context = {
                'form': form,
                'error': True,
            }
        return render(request, 'core/login.html', context)
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'core/login.html', context)


def register(request):
    return render(request, 'core/register.html')


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


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
