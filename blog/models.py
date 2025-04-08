from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name="Título",
        max_length=200,
    )
    content = models.TextField(
        verbose_name="Contenido",
        )
    author = models.CharField(
        verbose_name="Autor",
        max_length=100,
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        default=timezone.now,
    )

    def __str__(self):
        return self.title

# python manage.py makemigrations en la terminal y python manage.py migrate
# Luego voy a admin.py y registro el modelo Post para que se vea en el admin.
