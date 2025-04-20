"""
URL configuration for firstpage_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns

# Rutas sin prefijo de idioma (no traducibles)
urlpatterns = [
    path('rosetta/', include('rosetta.urls')),
    path('set-language/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Rutas con prefijo de idioma (sí traducibles)
urlpatterns += i18n_patterns(
    path("", include("core.urls", namespace="core")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("cursos/", include("courses.urls", namespace="courses")),
)
