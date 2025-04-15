from django.contrib import admin

from .models import Contact  # En caso de fallo del mail


# Register your models here.
@admin.register(Contact)  # En caso de fallo del mail
class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ("nombre", "contactado", "email", "created_at")
    list_filter = ("contactado",)
