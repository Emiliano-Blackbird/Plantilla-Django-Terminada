from django.contrib import admin

# Register your models here.
from .models import Course


@admin.register(Course)
class CourseResource(admin.ModelAdmin):
    model = Course
    list_display = ("title", "Created_At")
