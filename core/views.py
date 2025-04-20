# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages  # Mensajes de información
from django.utils.translation import gettext as _
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.utils import translation

from courses.models import Course
from blog.models import Post
from .forms import ContactForms, LoginForm, UserRegisterForm
from django.core.mail import send_mail
from .models import Contact  # En caso de fallo del mail
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect  # Redireccionar a otra vista
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView


# Vistas generales de la app
def home(request):
    context = {
        'courses': Course.objects.filter(show_home=True),
        'posts': Post.objects.filter(show_home=True),
    }
    return render(request, 'core/home.html', context)


class HomeView(TemplateView):  # Vista basada en clase (CCBV)
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):  # Función más escalable y modular
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(show_home=True)
        context['posts'] = Post.objects.filter(show_home=True)

        messages.info(self.request, _("Mensaje de información"))  # Mensaje info
        return context


class HomeView2(HomeView):  # Template view (CCBV) hereda todo en home2
    template_name = 'core/home2.html'


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
                messages.success(request, f'Has iniciado sesión correctamente, {user.username}!')
                return redirect(reverse("core:home"))
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': _('Usuario no valido'),
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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # Creamos el usuario
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Mensaje de éxito
            messages.success(request, _('¡Usuario creado correctamente! Ya puedes iniciar sesión.'))

            return redirect('core:login')  # Redirigimos a la página de login

        else:
            context = {
                'form': form,
                'error': True,
            }
            return render(request, 'core/register.html', context)

    else:
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'core/register.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, _('Has cerrado sesión correctamente.'))  # Mensaje de éxito
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


class SetLanguageView(View):
    def post(self, request, *args, **kwargs):
        language = request.POST.get('language', None)
        request.session[translation.LANGUAGE_SESSION_KEY] = language

        if language:
            translation.activate(language)

        next_url = request.POST.get('next', '/')
        return HttpResponseRedirect(next_url)
