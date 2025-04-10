# Create your models here.
from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField  # asegurate de tener instalado django-ckeditor


# Create your models here.
class Course(models.Model):
    title = models.CharField(
        verbose_name="Título del curso",
        max_length=200,
    )
    content = RichTextField(
        verbose_name="Contenido del curso",
        )
    Enlace_Oficial = models.URLField(
        verbose_name="Enlace oficial a Django",
    )
    Created_At = models.DateTimeField(
        verbose_name="Fecha de creación",
        default=timezone.now,
    )

    show_home = models.BooleanField(
        'Mostrar en la home',
        default=False,
    )
    toc = models.FileField(
        verbose_name="Temario",
        upload_to="courses/toc/",  # directorio donde se guardará el archivo subido por el usuario
        null=True,
        blank=True,
    )
    course_image = ImageField(
        verbose_name="Portada del curso",
        upload_to="courses/images/",  # directorio donde se guardará el archivo subido por el usuario
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
# python manage.py makemigrations en la terminal y python manage.py migrate
# Voy a admin.py y registro el modelo Post para que se vea en admin.
