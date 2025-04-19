# Para definir las urls de la app core

from django.urls import path

from .views import home, about_us, login_view, register, contact, logout_view, HomeView, HomeView2

app_name = 'core'  # Nombre del namespace de la app blog

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # Vista de la página de inicio
    path("home2", HomeView2.as_view(), name="home2"),  # Vista página de inicio 2
    path("sobre-nosotros/", about_us, name="about_us"),
    path("registro/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("contacta-con-nosotros/", contact, name="contact"),
]
