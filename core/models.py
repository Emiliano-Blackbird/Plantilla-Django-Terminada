from django.db import models
from django.utils import timezone


# Create your models here. (make y migrate)
class Contact(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=50,
    )
    email = models.EmailField(
        verbose_name="Email",
    )
    comentario = models.TextField(
        verbose_name="Comentario que ha dejado en la web",
        max_length=500,
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha y hora de creación",
        default=timezone.now,
    )  # En caso de fallo del mail se registrará en base de datos
    contactado = models.BooleanField(
        verbose_name="¿Se ha contactado con el usuario?",
        default=False,
    )

    def __str__(self):
        return self.nombre
