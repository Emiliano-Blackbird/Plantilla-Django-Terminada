# Generated by Django 5.2 on 2025-04-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Contactado',
            field=models.BooleanField(default=False, verbose_name='¿Se ha contactado con el usuario?'),
        ),
    ]
