from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostResource(admin.ModelAdmin):
    model = Post
    list_display = ("title", "pk", "show_home", "author", "created_at")
