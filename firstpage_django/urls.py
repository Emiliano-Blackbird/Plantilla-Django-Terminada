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
