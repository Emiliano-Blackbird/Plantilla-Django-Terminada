# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.
class Course(models.Model):
    title = models.CharField(
        verbose_name="Título del curso",
        max_length=200,
    )
    content = models.TextField(
        verbose_name="Contenido del curso",
        )
    Enlace_Oficial = models.URLField(
        verbose_name="Enlace oficial a Django",
    )
    Created_At = models.DateTimeField(
        verbose_name="Fecha de creación",
        default=timezone.now,
    )

    def __str__(self):
        return self.title
# python manage.py makemigrations en la terminal y python manage.py migrate
# Voy a admin.py y registro el modelo Post para que se vea en admin.
